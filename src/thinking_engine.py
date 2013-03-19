'''
Created on 15-Mar-2013

@author: iamrock

    This class is the thinking Engine - That means that this class will have the
    logic for interaction of various objects!!!
'''

import pyglet, time
from pyglet.window import key
from pyglet.image.codecs.png import PNGImageDecoder
import sys

class Engine():
    '''
         This class contains the main logic, from the levels, to the game logic and engine (very basic engine)
    '''


    def __init__(self):
        '''
        Constructor
        '''
        window = self.init_window(400,400)
        self.start_game(window)
        
        pyglet.app.run()
    
    def collide_x(self, x):
        ''' 
            Checks for x collision
        '''

        # Transform the position of the world to uniform axis (0,0) 
    
        X  = [50,350]
    

        if (x) in X:
            return True
        if (x) in X:
            return True
    
        return False

    
    def collide_y(self, y):
        ''' 
    
            Check for Y axis collision
        '''

        Y = [50,300]    
        
        if (y) in Y:
            return True
        if (y) in Y:
            return True

        return False
    
    
    def init_window(self, SCREEN_H, SCREEN_W):
        '''
            This will be the graphics window of the game. This will contain the window properties.
        '''
        
        # Call the default constructor of pyglet for initialization of openGL window.
        mainWindow = pyglet.window.Window(SCREEN_H, SCREEN_W, caption = "Thinking Tank")
        
        # Place the window at the center of the desktop
        mainWindow.set_location(mainWindow.screen.width/2 - mainWindow.width/2, 
                                mainWindow.screen.height/2 - mainWindow.height/2)
        
        # Start the main loop
        
        
        return mainWindow
        
      

    def start_game(self, window):
        '''
            This method will start the game by doing the following actions :
                load sprites 
                map new keys
                
                display level 1 sprites
                if progress then display level 2 sprites
                else main menu
                if progress then display level 3 sprites
                else main menu
                
                on M main menu
                on R load level 1
                
        '''

        
        '''
            Load all the sprites
        '''     
        # Tank 
        img_tank = pyglet.image.load('res/images/sprites/Level 1/Tank.png', decoder=PNGImageDecoder())
        img_tank.anchor_x = 25
        img_tank.anchor_y = 25
            
        #  Convert it to sprite
        tank = sprite_tank = pyglet.sprite.Sprite(img_tank)
        sprite_tank.x = 175
        sprite_tank.y = 175
            
        # Level 1 Graphics
        img_level1 = pyglet.image.load('res/images/sprites/Level 1/Level1.png', decoder=PNGImageDecoder())
        sprite_level1 = pyglet.sprite.Sprite(img_level1)


        sprite_level1.x = 0
        sprite_level1.y = 0 
                
        KEYMAP = key.KeyStateHandler()
        
        
        def map_keys(dt):
            '''
               This method is responsible for mapping keys 
               The following keys are used in this game :
    
                    1. UP - Tank Up
                    2. DOWN - Tank Down
                    3. LEFT - Tank Left
                    4. RIGHT - Tank Right
                    5. ESC - Exit.
                    6. Enter - Select menu item.
                    7. M - Main Menu
                    8. R - Reload Level
            '''
            # Push the custom defined KEYMAP key handlers into the main loop
            window.push_handlers(KEYMAP)
            
            if KEYMAP[key.DOWN]:
                key_pressed('DN')
            
            elif KEYMAP[key.UP]:
                key_pressed('UP')
            
            elif KEYMAP[key.LEFT]:
                key_pressed('LT')
            
            elif KEYMAP[key.RIGHT]:
                key_pressed('RT')
            
            elif KEYMAP[key.M] :
                key_pressed('M')
                
            elif KEYMAP[key.R] :
                key_pressed('R')
                
            elif KEYMAP[key.ESCAPE] :
                sys.exit()     
            
        def key_pressed(key):
            
            if 'UP' in key:
                if tank._rotation.__pos__() == 0:
                    # Check for collission
                    if not self.collide_y(tank.y) :
                        tank.y += 1
                    else :
                        tank.y -= 5
                else :    
                    tank._set_rotation(0.0)
                    time.sleep(0.10)
                    
            if 'DN' in key:
                if tank._rotation.__pos__() == 180:    
                    # Check for collission
                    if not self.collide_y(tank.y) :
                        tank.y -= 1
                    else :
                        tank.y += 5
                else :
                    tank._set_rotation(180.0)
                    time.sleep(0.10)
                    
            if 'LT' in key:
                if tank._rotation.__pos__() == 270:
                # Check for collission
                    if not self.collide_x(tank.x) :
                        tank.x -= 1
                    else :
                        tank.x += 5
                else :
                    tank._set_rotation(270.0)
                    time.sleep(0.10)
                
            if 'RT' in key:
                
                if tank._rotation.__pos__() == 90:
                # Check for collission
                    if not self.collide_x(tank.x) : 
                        tank.x += 1
                    else :
                        tank.x -= 5
                else :
                    tank._set_rotation(90.0)
                    time.sleep(0.10)
                
            if 'M' in key:
                window.close()
                
            if 'R' in key :
                pass
        
        
        
        
        @window.event
        def on_draw():
            window.clear()
            sprite_level1.draw()
            sprite_tank.draw()
        
        @window.event
        def on_mouse_press(x, y, button, modifiers):
            print 'X,Y:' + `x` + ',' + `y`
        
        pyglet.clock.schedule_interval(map_keys, 1.0/60.0)    
    
         



            
        
                
            