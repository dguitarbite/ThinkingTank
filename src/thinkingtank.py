#!/usr/bin python2.7 

'''
Created on 08-Feb-2013

@author: iamrock/dguitarbite - dguitarbite@gmail.com
@license: GPLv3
@repository: http://www.github.com/ThinkingTank
@team : Other team members :
	Pranav Salunke/dguitarbite - dguitarbite@gmail.com - programming + game design
	Ritesh Puj - nnsjw702@gmail.com - Documentation + Repository Management
	Fenil Shah - fenilshah2013@gmail.com - Music + Documentation
	Ajyanka More - ajinkyamoray@gmail.com - Graphics + Documentation
	Akshay Ajgaokar - akshayajgaonkar@gmail.com - Graphics + Documentation
@about: Refer the documentation in the ./docs folder.
 * ----------------------------------------------------------------------
 * ---------------------Welcome to Thinking Tank ------------------------
 * ----------------------------------------------------------------------
 * 


 * This is a simple game which will make your brains work !!!
 * well I and my team will try our best to match the hype 
 * Thanks a lot for going through the source code.
 * 
 * Just a brief explanation to the Module Structure and break down :
 *      1) Packages Hierarchy -
 *              Well I'm at the beginning of Expert Programmer for Python and OOPS
 *              so I have taken the liberty of skipping Inheritance among the classes.
 *				that is where I could skip inheritance. There are some method overrides
 *              but its pyglet not me!!!. I'm just using it.
 * 

	This game uses Pyglet -- a simpler version of OpenGl for python.
	
	Control Flow?
'''

import main_menu

class ThinkingTank :
	'''
		This class is responsible for loading various properties, text , images , dependences.
		This class should also contain the information for levels.
	'''
	
	def __init__(self):
		'''
			/!\	Customized Constructor
			
			I'm planning to load a few splash screens, some logos then the graphics.
			Also this should load the music , then fade in the menu from black.
			Then its the user who kind of decides what to do with the language.
		'''
		
		#call the Graphics method to start the openGl graphics window.
		main_menu.Main_Menu()
		

	


	def load_level(self) :
		'''
			This game has three levels.
				This method will load the classes that contain level
				design, description and other level related code.
				1. Level 1 - This will be a simple level for introduction to the game. The aim is to warm up your brains.
				2. Level 2 - This will be a bit tougher, will rack your brains.
				3. Level 3 - This will be the toughest, grab some coffee!
		'''

		pass

	
	def difficulty(self) :
		'''
			This game has three difficulty levels.
			This module will activate or deactivate features as per the difficulty.
			Difficulty Levels - 
				1. Noob --> easy.
					No time and no of moves constraints.
				2. Geek --> Medium.
					Time and no of moves will affect the score.
				3. Einstein --> Difficult.
					If you don't finish the level in the given
					time , the player will lose.
		'''

		pass


	def load_music(self) :
		'''
			Loads the required music files.
		'''

		pass 

	def load_graphics(self):
		'''
			This method is responsible to load the graphics.
		'''
		
		pass




class Levels :
	'''
		
	'''

#start the game.
startgame = ThinkingTank()
