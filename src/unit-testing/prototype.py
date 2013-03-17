import pyglet
from pyglet.window import key


#screen size
SCREEN_H = 1200
SCREEN_W = 900

#Simple tank size :
TANK_W = 8
TANK_H = 8


#Set title --
window = mainWindow = pyglet.window.Window(SCREEN_H, SCREEN_W, caption="Thinking Tank")

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


def update():
	pyglet.clock.schedule_interval(move, 1.0/60.0)


def move(dt):
	mainWindow.push_handlers(KEYMAP)
	
	
	if KEYMAP[key.DOWN]:
		label.y -= 1
	elif KEYMAP[key.UP]:
		label.y += 1
	elif KEYMAP[key.LEFT]:
		label.x -= 1
	elif KEYMAP[key.RIGHT]:
		label.x += 1
		


	


print 'Loading Label - Text',
print '.',
print '.',
print '.'



print '''Loading Background Image ''',
print '.',
print '.',
print '.'



#image = pyglet.resource.image('dawn of ubuntu.png')
print 'Loading Audio',
print '.',
print '.',
print '.'


#music = pyglet.resource.media('Crazy Dreams.mp3')


@window.event
def on_draw():
	window.clear()
	#image.blit(0, 0)
	label.draw()

#music.play()

@window.event
def on_key_press(symbol, modifiers):
    print 'keypressed !!!\nKeyCode:' + `symbol`
    # Handles the key presses.
    update()

pyglet.app.run()
