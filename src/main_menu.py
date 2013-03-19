'''
Created on 14-Mar-2013

@author: iamrock/dguitarbite - dguitarbite@gmail.com
@license: GPLv3
@repository: http://www.github.com/ThinkingTank

'''

import sys, time
import thinking_engine
import pyglet
from pyglet.window import key
from pyglet.image.codecs.png import PNGImageDecoder


class Main_Menu(object):
    '''
    
    This is a heavy Graphics file which contains of the following functionality.
    
    1. Call On game startup will lead to starting of the Splash, Logos and then the Main Menu.
    2. This is kind of like the Graphics Frame work for the game for the sake of handling all the required graphics files.
     
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
 
        mainWindow = self.init_window(1200,900)
        self.main_menu(mainWindow)
       
        # Call the OpenGL Main Loop
        pyglet.app.run()
 
        
        
    def main_menu(self,window):
        '''
            The main menu will consist of
            
                1. Labels :
                        Main Menu
                        ---------
                        Start Game
                        Help
                        Exit
        '''
            
 
            
        # Title of the Menu
        label_header = pyglet.text.Label("Main Menu",
                                                font_name='Ubuntu',
                                                font_size=48,
                                                bold = True,
                                                color=(255, 155, 55, 255), 
                                                x=window.width/2, y=700,
                                                anchor_x='center',
                                                anchor_y='center')
            
            
        # Menu Item 1
        label_menu1 = pyglet.text.Label("Start Game",
                                                font_name='Ubuntu',
                                                font_size=28, 
                                                x=window.width/2, y=500,
                                                anchor_x='center',
                                                anchor_y='center')
        # Menu Item 2
        label_menu2 = pyglet.text.Label("Help",
                                                font_name='Ubuntu',
                                                font_size=28, 
                                                x=window.width/2, y=400,
                                                anchor_x='center',
                                                anchor_y='center')
        # Menu Item 3
        label_menu3 = pyglet.text.Label("Exit",
                                                font_name='Ubuntu',
                                                font_size=28, 
                                                x=window.width/2, y=300,
                                                anchor_x='center',
                                                anchor_y='center')
            
                        
            
        # Add labels to OpenGL Window.
        @window.event
        def on_draw():
            window.clear()
            label_header.draw()
            label_menu1.draw()
            label_menu2.draw()
            label_menu3.draw()
            
        
        # Keyboard Mapper. Will decide what the pressed key will do!!!.
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
            # Push the custom defined KEYMAP key handlers into the main loop
            window.push_handlers(KEYMAP)
            
            if KEYMAP[key.DOWN]:
                key_pressed('DN')
            
            elif KEYMAP[key.UP]:
                key_pressed('UP')
                 
            elif KEYMAP[key.ENTER]:
                key_pressed('Ret')
                
            elif KEYMAP[key.ESCAPE]:
                sys.exit()
                
     
        
        def key_pressed(keys):
            '''
                This method will define the actions preceding the key pressed
                Types of keys are : 
                1. UP
                2. DN
                3. Ret
            '''

            
            def get_Label():
                '''
                    Gets the selected Label
                '''
                
                
                if label_menu1._get_bold() :
                    return 1
                elif label_menu2._get_bold() :
                    return 2
                elif label_menu3._get_bold() :
                    return 3
                
                return 3
            
            def set_label(old, new):
                '''
                    Sets the new label bold
                    and resets the older Label.
                '''
                if old == 1 :
                    label_menu1._set_bold(False)
                elif old == 2 :
                    label_menu2._set_bold(False)
                elif old == 3 :
                    label_menu3._set_bold(False)
                    
                if new == 1 :
                    label_menu1._set_bold(True)
                elif new == 2 :
                    label_menu2._set_bold(True)
                elif new == 3 :    
                    label_menu3._set_bold(True)
                
            if 'UP' in keys :
                
                old = get_Label()
                
                # Get New - Handy Logic - if new - 1 == 0 then it must point to 3 :D
                if old-1 != 0 :
                    new = old - 1
                else :
                    new = 3
                    
                set_label(old,new)

            elif 'DN' in keys :
                
                old = get_Label()
                
                # Something Similar to the UP key - if its 4 then it must point to 1 ;D
                if old + 1 != 4:
                    new = old + 1
                else :
                    new = 1
                
                set_label(old,new)
                # Get Old 
                
            elif 'Ret' in keys :
                
                selected_Label = get_Label()
                
                if selected_Label == 1 :
                    print 'Start Game'
                    thinking_engine.Engine()
                    # Call the start game method
                    return True 
                        
                    
                elif selected_Label == 2 :
                    pass
                                    
                elif selected_Label == 3 :
                    # Exit - Terminate the Game on EXit.                    
                    sys.exit()
                    
                        
     
        pass
    
        @window.event
        def on_key_press(symbol, modifiers):
            map_keys()
        
        
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
        
