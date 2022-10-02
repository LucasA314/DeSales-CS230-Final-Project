# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:43:20 2022

@author: lucas
"""

from constants import *
from core import *

from font_scripts import *

class obj_textbox(Object):
	def __init__(self):
		Object.__init__(self, "spr_textbox", 1, True)
	
	def create(self, main):
		#Initialize Variables

		self.current_message = ""					 #The unformatted message to be displayed.
		self.formatted_message = []				     #The formatted message to be displayed.
		self.current_paragraph = 0					 #An indicator of which paragraph of the message is on display.
		self.current_line = 0						 #An indicator of which line of the message is on display.
		self.current_character = -1				     #An indicator of which character of the message is set to display.
		self.frame_delay = 0						     #How many frames to wait between displaying letters as denoted by the text speed
		self.current_message_array = []               #The array with the letter sprites being displayed.
		self.message_timer = -1					     #A counter for messages that go away on a timer.
		self.options_event = False					 #A flag checking if the dialogue inculdes choices.
		self.text_done = False						 #A flag denoting if the text is done displaying.
		
		
		#Create the Cursor
		self.cursor = instance_create(main, self.x, self.y, obj_textbox_cursor())
		
		return main
	
	def update(self, main):
		#Run Dialogue

		#Set the Position on Screen
		self.x = 0
		self.y = 320
		
		#Set Cursor Position
		self.cursor.x = 144
		self.cursor.y = 352
		
		
		#If: Show the Sprite if there is Dialouge to be Displayed
		if (main.sub_state == GAME_STATES.DIALOGUE.value):
			
			
			self.message = self.formatted_message
			self.x_offset = 8
			self.y_offset = 16
			self.num_paragraphs = array_length(self.formatted_message)
			self.num_lines = array_length(self.formatted_message[self.current_paragraph])
			
			#Hide the Cursor
			self.cursor.visible = False
		
		
			#If There is More than One Line Left to Show, 
			#Then Display Two Lines In the Box
			if (self.current_line + 1 < self.num_lines):
			
				self.message_string = self.message[self.current_paragraph][self.current_line] + "\n" + self.message[self.current_paragraph][self.current_line + 1]	
			
			#Display One Line in the Box
			else:
			
				self.message_string = self.message[self.current_paragraph][self.current_line]
			
			
			if (self.current_character < len(self.message_string)):
			
				if (self.frame_delay == 0):
				
					self.current_message_array = scr_reset_letters(self.current_message_array)
					self.current_character += 1
					self.frame_delay = main.text_speed
				
				else:
				
					self.frame_delay -= 1	
				
			
			
			self.current_message_array = scr_place_object_text(main, self, self.current_message_array, self.x_offset, self.y_offset, CENTER_LEFT, self.message_string[0:self.current_character])
			
			#Show the Cursor
			if (self.current_line + 2 < self.num_lines or self.current_paragraph + 1 < self.num_paragraphs):
			
				self.cursor.visible = True
			
			else:
			
				self.cursor.visible = False	
			
		
			if (self.current_line + 2 >= self.num_lines and self.message_timer > 0):
			
				self.message_timer -= 1
			
			
			if (self.options_event and self.current_character >= len(self.message_string) - 1 and self.current_line + 2 >= self.num_lines and self.current_paragraph + 1 >= self.num_paragraphs):
			
				self.text_done = True
			
		
			#If: The Player Presses A
			if ((main.im.a or main.im.b or self.message_timer == 0) and (not self.options_event or not main.options_event_open)):
			
				main.im.a = False
				main.im.b = False
				
				if (self.current_character < len(self.message_string) - 1):
				
					self.current_character = len(self.message_string) - 1
				
				
				#If:   There are More Lines to Show
				#Then: Increase current_line by 1
				elif (self.current_line + 2 < self.num_lines):
				
					self.current_line += 1
					self.current_character = len(self.message[self.current_paragraph][self.current_line - 1])
					self.current_message_array = scr_reset_letters(self.current_message_array)
				
				elif (self.current_paragraph + 1 < self.num_paragraphs):
				
					self.current_paragraph += 1
					self.current_line = 0
					self.current_character = 0
					self.current_message_array = scr_reset_letters(self.current_message_array)
				
				#Else: Continue the Script Calling Upon the Dialog
				elif (not self.options_event):
				
					self.message_timer = -1
					self.current_paragraph = 0
					self.current_line = 0
					self.text_done = True
					self.current_message_array = scr_reset_letters(self.current_message_array)
				
			
		
		#Else: Otherwise, Hide the Box and Reset the Variables
		else:
			self.cursor.visible = False
			self.text_done = False
			self.options_event = False
			self.current_message = ""
			self.current_paragraph = 0
			self.current_line = 0
			self.current_character = -1
			self.frame_delay = 0
			self.current_message_array = scr_reset_letters(self.current_message_array)
		
				
		return main
	
	
class obj_textbox_cursor(Object):
	def __init__(self):
		Object.__init__(self, "spr_text_cursor", 1, False)