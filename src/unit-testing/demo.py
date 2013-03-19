
import pyglet
from pyglet.gl import *

from collide import *

# create a simple window
window = pyglet.window.Window(640, 480, caption="collision", visible=False)

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0) 
foreground = pyglet.graphics.OrderedGroup(1)

# load our images
block = pyglet.resource.image('images/block.png')
world = pyglet.resource.image('images/world.png')

class Entity(pyglet.sprite.Sprite):
	'''Movable, collidable entity class'''
	
	def __init__(self, image, x, y, batch, group):
		pyglet.sprite.Sprite.__init__(self, image, x, y, batch=batch, group=group)
		
		# create a collision structure for this sprite
		self.collision = SpriteCollision(self)
		
		# stay alive for 4 seconds
		self.life = 4.0

# create the level as an entity
level = Entity(world, 0, 0, batch, background)

# create a set to contain the blocks
# a set has a very fast difference operation,
# which we will use in the update function
blocks = set()

@window.event
def on_mouse_press(x, y, button, modifiers):
	'''Create a new block whenever the user clicks the mouse'''
	
	# create a new block
	b = Entity(block, x, y, batch, foreground)
	# add it to the set
	blocks.add(b)

@window.event
def on_draw():
	# clear the window
	window.clear()
	
	# draw our background and blocks
	batch.draw()

def update(dt):
	# we need to set the blocks variable, so declare it global
	global blocks
	
	for b in blocks:
		# don't let block fall out of the window bounds
		if b.y < 0:
			b.y = 0
		
		# apply gravity
		b.y -= 8
		
		# move the block back upwards if they collide
		while collide(b.collision, level.collision):
			b.y += 1
		
		# reduce the block's lfe
		b.life -= 1/30.0
	
	# use a generator expression to construct a new set containing only the dead blocks
	dead = set(b for b in blocks if b.life <= 0.0)
	
	# remove the dead blocks from the render batch
	for b in dead:
		b.batch = None
	
	# use a set difference operation to remove the dead blocks from the update set
	blocks = blocks.difference(dead)

glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# make the window visible
window.set_visible(True)

# schedule our update function
pyglet.clock.schedule_interval(update, 1/30.0)

# and finally, run the app...
pyglet.app.run()
