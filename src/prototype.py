import pyglet
from pyglet.window import key
#Window Size --
#win = window.Window(fullscreen=True, vsync=True)
#win = pyglet.window.Window(640, 480, resizable=True, visible=True)


#Set title --

window = pyglet.window.Window(1200, 900)

window.set_caption("Thinking Tank - Prototype - Game Programming -")

Message = 'Basic Keyboard and Mouse Events'




label = pyglet.text.Label(Message,
font_name='Ubuntu',
font_size=36,
x=window.width/2, y=35,
anchor_x='center', anchor_y='center')

print 'Loading Label - Text',
print '.',
print '.',
print '.'



print '''Loading Background Image ''',
print '.',
print '.',
print '.'


#image = pyglet.resource.image('dawn of ubuntu.png')
image = pyglet.resource.image('dawn of ubuntu.png')
print 'Loading Audio',
print '.',
print '.',
print '.'


music = pyglet.resource.media('Crazy Dreams.mp3')


@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)
	label.draw()
	
@dispatcher.event
def on_key_press():
	if keys[key.ENTER]:
		print 'ENTER'

music.play()

keys = key.KeyStateHandler()
window.push_handlers(keys)





pyglet.app.run()
