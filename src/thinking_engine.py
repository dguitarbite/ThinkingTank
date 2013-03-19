'''
Created on 15-Mar-2013

@author: iamrock

    This class is the thinking Engine - That means that this class will have the
    logic for interaction of various objects!!!
'''

import pyglet
from pyglet.window import key
import sys

class Engine(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        window = self.init_window(400,400)
        self.start_game(window)
    
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
        
         
                
        KEYMAP = key.KeyStateHandler()
        
        def map_keys():
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
            
            elif KEYMAP[key.ENTER]:
                key_pressed('Ret')
            
            elif KEYMAP[key.M] :
                key_pressed('M')
                
            elif KEYMAP[key.R] :
                key_pressed('R')
                
            elif KEYMAP[key.ESCAPE] :
                sys.exit()     
            
        def key_pressed(key):    
            pass
        def level1(difficulty) :
            pass
        def level2(difficulty) :
            pass
        def level3(difficulty) :
            pass
        
        @window.event
        def on_draw():
            window.clear()
            
        
        @window.event
        def on_key_press(symbol, modifiers):    
            map_keys()
