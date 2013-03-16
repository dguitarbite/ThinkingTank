'''
Created on 14-Mar-2013

@author: iamrock/dguitarbite - dguitarbite@gmail.com
@license: GPLv3
@repository: http://www.github.com/ThinkingTank

'''

import pyglet
from pyglet.window import key
from pyglet.image.codecs.png import PNGImageDecoder


class Graphics(object):
    '''
    
    This is a heavy Graphics file which contains of the following functionality.
    
    1. Call On game startup will lead to starting of the Splash, Logos and then the Main Menu.
    2. This is kind of like the Graphics Frame work for the game for the sake of handling all the required graphics files.
     
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        mainWindow = self.main_window()
        self.main_menu(mainWindow)
        self.load_sprites(mainWindow)
       
        # Call the OpenGL Main Loop
        pyglet.app.run()
 
        
        
    def main_menu(self,window):
        '''
            The main menu will consist of 
        '''    
                
        main_menu_label = pyglet.text.Label("Main Menu",
                          font_name='Ubuntu',
                          font_size=48, 
                          x=window.width/2, y=800,
                          anchor_x='center',
                          anchor_y='center')
        # Keyboard Mapper.
        KEYMAP = key.KeyStateHandler()
        
        def map_keys():
            '''
               This method is responsible for mapping keys 
               The following keys are used in this game :
    
                    1. UP - Menu Up
                    2. DOWN - Menu Down
                    3. LEFT - Menu Left
                    4. RIGHT - Menu Right
                    5. ESC - Exit.
                    6. Enter - Select menu item.
            '''
            window.push_handlers(KEYMAP)
            
            if KEYMAP[key.DOWN]:
                key_pressed('DN')
            
            elif KEYMAP[key.UP]:
                key_pressed('UP')
            
            elif KEYMAP[key.LEFT]:
                pass
            
            elif KEYMAP[key.RIGHT]:
                pass
            
            elif KEYMAP[key.ENTER]:
                key_pressed('Ret')    
        
        def key_pressed(key):
            '''
                This method will define the actions preceding the key pressed
                Types of keys are : 
                1. UP
                2. DN
                3. Ret
            '''
            if 'UP' in key :
                print 'Up key pressed on main menu'
            elif 'DN' in key :
                print 'Down Key Pressed on main menu'
            elif 'Ret' in key :
                print 'Enter Key Pressed on main menu'
            else :
                pass
            
            
        @window.event
        def on_draw():
            window.clear()
            main_menu_label.draw()
                    
        pass
    
        @window.event
        def on_key_press(symbol, modifiers):
            map_keys()
        
        
    def main_window(self):
        '''
            This will be the graphics window of the game. This will contain the window properties.
        '''
        # Height of the screen
        SCREEN_H = 1200
        #Width of the screen
        SCREEN_W = 900
        
        # Call the default constructor of pyglet for initialization of openGL window.
        mainWindow = pyglet.window.Window(SCREEN_H, SCREEN_W, caption = "Thinking Tank")
        
        # Place the window at the center of the desktop
        mainWindow.set_location(mainWindow.screen.width/2 - mainWindow.width/2, 
                                mainWindow.screen.height/2 - mainWindow.height/2)
        
        # Start the main loop
        
        
        return mainWindow
        
        
    def load_sprites(self,window):
        '''
            The basic sprites which will be required for the game:
            
                1. Tank
                2. Rock
                3. Wall
                4. Goal Tile
                6. Normal Tile
                7. Boundary
                8. Display Score/Time/Level/Difficulty.
                9. Background Music
        '''
        
        pass
    
    
    def map_keys(self):
        '''
            This method is responsible for mapping keys 
            The following keys are used in this game :
                
                1. UP - Move Tank Up.
                2. DOWN - Move Tank Down.
                3. LEFT - Move Tank Left.
                4. RIGHT - Move Tank Right.
                5. R - Reset Level.
                6. M - Main Menu.
                7. ESC - Exit.
                8. Enter - Select menu item.
        '''
        
        pass
