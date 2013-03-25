import pyglet
from pyglet.window import key
from pyglet.image.codecs.png import PNGImageDecoder
import time


#screen size
SCREEN_H = 1200
SCREEN_W = 900

#Simple tank size :
TANK_W = 8
TANK_H = 8


#Set title --
window = mainWindow = pyglet.window.Window(SCREEN_H, SCREEN_W, caption="Thinking Tank" )
window.set_icon = pyglet.image.load("Tank.png")


# Center window.
mainWindow.set_location(mainWindow.screen.width/2 - mainWindow.width/2, mainWindow.screen.height/2 - mainWindow.height/2)

#keyboard
KEYMAP = key.KeyStateHandler()

Message = 'Basic Keyboard and Mouse Events'




label = pyglet.text.Label(Message,
                          font_name='Ubuntu',
                          font_size=36, 
                          x=window.width/2, y=35,
                          anchor_x='center',
                          anchor_y='center')


# Call update 60 times a second.


def update():
	pyglet.clock.schedule_interval(move, 1.0/30.0)


def move(dt):
	mainWindow.push_handlers(KEYMAP)
	
	
	if KEYMAP[key.DOWN]:
		if sprite._rotation.__pos__() == 180:	
			sprite.y -= 1
		else :
			sprite._set_rotation(180.0)


	elif KEYMAP[key.UP]:
		if sprite._rotation.__pos__() == 0:
			sprite.y += 1
		else :	
			sprite._set_rotation(0.0)
		tank_rotation = 'up'


	elif KEYMAP[key.LEFT]:
		if sprite._rotation.__pos__() == 270:
			sprite.x -= 1
		else :
			sprite._set_rotation(270.0)
		tank_rotation = 'lt'


	elif KEYMAP[key.RIGHT]:
		if sprite._rotation.__pos__() == 90:
			sprite.x += 1
		else :
			sprite._set_rotation(90.0)
		tank_rotation = 'rt'

		


	


print 'Loading Label - Text',
print '.',
print '.',
print '.'



print '''Loading Background Image ''',
print '.',
print '.',
print '.'



image = pyglet.resource.image('Bk-Ground.png')
print 'Loading Audio',
print '.',
print '.',
print '.'


music = pyglet.resource.media('upbeat2(with guitar + melodica).mp3')
tank = pyglet.image.load('Tank.png', decoder=PNGImageDecoder())
tank.anchor_x = 50
tank.anchor_y = 50

sprite = pyglet.sprite.Sprite(tank)

wall = pyglet.image.load('Carpet.png', decoder=PNGImageDecoder())
sprite_wall = pyglet.sprite.Sprite(wall)

goal = pyglet.image.load('goal.png', decoder=PNGImageDecoder())



@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)
	label.draw()
	sprite.draw()

music.play()

@window.event
def on_key_press(symbol, modifiers):
    print 'keypressed !!!\nKeyCode:' + `symbol`
    # Handles the key presses.
    update()

pyglet.app.run()