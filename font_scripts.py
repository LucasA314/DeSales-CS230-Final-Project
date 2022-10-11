# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:00:39 2022

@author: lucas
"""

from constants import *
from core import *
from font_objects import *

import math



#Draw String
'''
	Draws a String that is Actually An Array of Font Indexes.
'''
def scr_draw_string(main, s_x, s_y, string, centering):

	spaceCounter = 0
	drawLine = 0
	current_message = []
	
	#Loop Through the String
	for i in range(len(string)):
	
		#Check for Characters with Unique Functions
		if (string[i][0] == LETTER_CONSTANTS.NEW_LINE.value - 1):
		
			drawLine += 1
			spaceCounter = 0
		
		elif (string[i][0] != LETTER_CONSTANTS.SPACE.value - 1 or spaceCounter != 0):
		
			#Create the New Letter and Store It for Future Deletion
			newLetter = instance_create(main, s_x + (spaceCounter * centering), s_y + (drawLine * 2 * LETTER_SPACING), obj_letter())			
			current_message.append(newLetter)
			
			#Alter Spacing for Apostrophe '
			if (string[i][0] == LETTER_CONSTANTS.APOSTROPHE.value - 1):
			
				newLetter.x -= 5
				spaceCounter -= 5
			
			
			#Set Up the Letter Sprite
			if (string[i][1] == LOWER):
			
				newLetter.sprite_index = "spr_lowercase_letters"
			
			else:
			
				newLetter.sprite_index = "spr_uppercase_letters"
			
		
			newLetter.image_index = math.ceil(string[i][0])
			newLetter.image_speed = 0
			
			#Create Space for the Next Letter
			spaceCounter += LETTER_SPACING
		
	
	
	return current_message



#Place Object Text
'''
	Draws a New String Only for Empty Message Containers, Allowing for the Statement To Run In Step Loops.
'''
def scr_place_object_text(main, obj, textArray, xoffset, yoffset, centering, textToDraw):

	if (len(textArray) == 0):

		textArray = scr_draw_string(main, obj.x + xoffset,  obj.y + yoffset, scrTranslateString(textToDraw), centering)
	
	
	return textArray


#Reset Letters
'''
	Wipes a message array to be deleted or rewritten.
'''
def scr_reset_letters(current_message):

	#Delete Each Letter
	for i in range(len(current_message)):
	
		current_message[i].eliminate = True
	
	
	#Delete the Existing List and Return a Fresh One
	current_message = []
	return []


# Translate Character
'''
	Translates a singular character into it's appropriate letter index.
'''
def scr_translate_character(char, letterSprite):
	
	if char == "a":
		finalChar = [LETTER_CONSTANTS.A.value - 1, LOWER]
		
	elif char == "b":
		finalChar = [LETTER_CONSTANTS.B.value - 1, LOWER]
		
	elif char == "c":
		finalChar = [LETTER_CONSTANTS.C.value - 1, LOWER]
		
	elif char == "d":
		finalChar = [LETTER_CONSTANTS.D.value - 1, LOWER]
		
	elif char == "e":
		finalChar = [LETTER_CONSTANTS.E.value - 1, LOWER]
		
	elif char == "f":
		finalChar = [LETTER_CONSTANTS.F.value - 1, LOWER]
		
	elif char == "g":
		finalChar = [LETTER_CONSTANTS.G.value - 1, LOWER]
		
	elif char == "h":
		finalChar = [LETTER_CONSTANTS.H.value - 1, LOWER]
		
	elif char == "i":
		finalChar = [LETTER_CONSTANTS.I.value - 1, LOWER]
		
	elif char == "j":
		finalChar = [LETTER_CONSTANTS.J.value - 1, LOWER]
		
	elif char == "k":
		finalChar = [LETTER_CONSTANTS.K.value - 1, LOWER]
		
	elif char == "l":
		finalChar = [LETTER_CONSTANTS.L.value - 1, LOWER]
		
	elif char == "m":
		finalChar = [LETTER_CONSTANTS.M.value - 1, LOWER]
		
	elif char == "n":
		finalChar = [LETTER_CONSTANTS.N.value - 1, LOWER]
		
	elif char == "o":
		finalChar = [LETTER_CONSTANTS.O.value - 1, LOWER]
		
	elif char == "p":
		finalChar = [LETTER_CONSTANTS.P.value - 1, LOWER]
		
	elif char == "q":
		finalChar = [LETTER_CONSTANTS.Q.value - 1, LOWER]
		
	elif char == "r":
		finalChar = [LETTER_CONSTANTS.R.value - 1, LOWER]
		
	elif char == "s":
		finalChar = [LETTER_CONSTANTS.S.value - 1, LOWER]
		
	elif char == "t":
		finalChar = [LETTER_CONSTANTS.T.value - 1, LOWER]
		
	elif char == "u":
		finalChar = [LETTER_CONSTANTS.U.value - 1, LOWER]
		
	elif char == "v":
		finalChar = [LETTER_CONSTANTS.V.value - 1, LOWER]
		
	elif char == "w":
		finalChar = [LETTER_CONSTANTS.W.value - 1, LOWER]
		
	elif char == "x":
		finalChar = [LETTER_CONSTANTS.X.value - 1, LOWER]
		
	elif char == "y":
		finalChar = [LETTER_CONSTANTS.Y.value - 1, LOWER]
		
	elif char == "z":
		finalChar = [LETTER_CONSTANTS.Z.value - 1, LOWER]
		
	elif char == "A":
		finalChar = [LETTER_CONSTANTS.A.value - 1, UPPER]
		
	elif char == "B":
		finalChar = [LETTER_CONSTANTS.B.value - 1, UPPER]
		
	elif char == "C":
		finalChar = [LETTER_CONSTANTS.C.value - 1, UPPER]
		
	elif char == "D":
		finalChar = [LETTER_CONSTANTS.D.value - 1, UPPER]
		
	elif char == "E":
		finalChar = [LETTER_CONSTANTS.E.value - 1, UPPER]
		
	elif char == "F":
		finalChar = [LETTER_CONSTANTS.F.value - 1, UPPER]
		
	elif char == "G":
		finalChar = [LETTER_CONSTANTS.G.value - 1, UPPER]
		
	elif char == "H":
		finalChar = [LETTER_CONSTANTS.H.value - 1, UPPER]
		
	elif char == "I":
		finalChar = [LETTER_CONSTANTS.I.value - 1, UPPER]
		
	elif char == "J":
		finalChar = [LETTER_CONSTANTS.J.value - 1, UPPER]
		
	elif char == "K":
		finalChar = [LETTER_CONSTANTS.K.value - 1, UPPER]
		
	elif char == "L":
		finalChar = [LETTER_CONSTANTS.L.value - 1, UPPER]
		
	elif char == "M":
		finalChar = [LETTER_CONSTANTS.M.value - 1, UPPER]
		
	elif char == "N":
		finalChar = [LETTER_CONSTANTS.N.value - 1, UPPER]
		
	elif char == "O":
		finalChar = [LETTER_CONSTANTS.O.value - 1, UPPER]
		
	elif char == "P":
		finalChar = [LETTER_CONSTANTS.P.value - 1, UPPER]
		
	elif char == "Q":
		finalChar = [LETTER_CONSTANTS.Q.value - 1, UPPER]
		
	elif char == "R":
		finalChar = [LETTER_CONSTANTS.R.value - 1, UPPER]
		
	elif char == "S":
		finalChar = [LETTER_CONSTANTS.S.value - 1, UPPER]
		
	elif char == "T":
		finalChar = [LETTER_CONSTANTS.T.value - 1, UPPER]
		
	elif char == "U":
		finalChar = [LETTER_CONSTANTS.U.value - 1, UPPER]
		
	elif char == "V":
		finalChar = [LETTER_CONSTANTS.V.value - 1, UPPER]
		
	elif char == "W":
		finalChar = [LETTER_CONSTANTS.W.value - 1, UPPER]
		
	elif char == "X":
		finalChar = [LETTER_CONSTANTS.X.value - 1, UPPER]
		
	elif char == "Y":
		finalChar = [LETTER_CONSTANTS.Y.value - 1, UPPER]
		
	elif char == "Z":
		finalChar = [LETTER_CONSTANTS.Z.value - 1, UPPER]
		
	elif char == "0":
		finalChar = [LETTER_CONSTANTS.ZERO.value - 1, LOWER]
		
	elif char == "1":
		finalChar = [LETTER_CONSTANTS.ONE.value - 1, LOWER]
		
	elif char == "2":
		finalChar = [LETTER_CONSTANTS.TWO.value - 1, LOWER]
		
	elif char == "3":
		finalChar = [LETTER_CONSTANTS.THREE.value - 1, LOWER]
		
	elif char == "4":
		finalChar = [LETTER_CONSTANTS.FOUR.value - 1, LOWER]
		
	elif char == "5":
		finalChar = [LETTER_CONSTANTS.FIVE.value - 1, LOWER]
		
	elif char == "6":
		finalChar = [LETTER_CONSTANTS.SIX.value - 1, LOWER]
		
	elif char == "7":
		finalChar = [LETTER_CONSTANTS.SEVEN.value - 1, LOWER]
		
	elif char == "8":
		finalChar = [LETTER_CONSTANTS.EIGHT.value - 1, LOWER]
		
	elif char == "9":
		finalChar = [LETTER_CONSTANTS.NINE.value - 1, LOWER]
		
	elif char == "-":
		finalChar = [LETTER_CONSTANTS.DASH.value - 1, LOWER]
		
	elif char == "?":
		finalChar = [LETTER_CONSTANTS.QUESTION.value - 1, LOWER]
		
	elif char == "!":
		finalChar = [LETTER_CONSTANTS.EXCLAMATION.value - 1, LOWER]
		
	elif char == "(":
		finalChar = [LETTER_CONSTANTS.PAR_L.value - 1, LOWER]
		
	elif char == ")":
		finalChar = [LETTER_CONSTANTS.PAR_R.value - 1, LOWER]
		
	elif char == ":":
		finalChar = [LETTER_CONSTANTS.COLON.value - 1, LOWER]
		
	elif char == "":
		finalChar = [LETTER_CONSTANTS.SEMICOLON.value - 1, LOWER]
		
	elif char == "[":
		finalChar = [LETTER_CONSTANTS.BRAC_L.value - 1, LOWER]
		
	elif char == "]":
		finalChar = [LETTER_CONSTANTS.BRAC_R.value - 1, LOWER]
		
	elif char == "#":
		finalChar = [LETTER_CONSTANTS.BACKSLASH.value - 1, LOWER]
		
	elif char == ".":
		finalChar = [LETTER_CONSTANTS.DOT.value - 1, LOWER]
		
	elif char == ",":
		finalChar = [LETTER_CONSTANTS.COMMA.value - 1, LOWER]
		
	elif char == "'":
		finalChar = [LETTER_CONSTANTS.APOSTROPHE.value - 1, LOWER]
		
	elif char == " ":
		finalChar = [LETTER_CONSTANTS.SPACE.value - 1, LOWER]
		
	elif char == "_":
		finalChar = [LETTER_CONSTANTS.UNDERSCORE.value - 1, LOWER]
		
	elif char == "\n":
		finalChar = [LETTER_CONSTANTS.NEW_LINE.value - 1, LOWER]
		
	elif char == "<PK_>":
		finalChar = [LETTER_CONSTANTS.PK.value - 1, LOWER]
		
	elif char == "<MN_>":
		finalChar = [LETTER_CONSTANTS.MN.value - 1, LOWER]
		
	elif char == "<M__>":
		finalChar = [LETTER_CONSTANTS.MALE.value - 1, LOWER]
		
	elif char == "<F__>":
		finalChar = [LETTER_CONSTANTS.FEMALE.value - 1, LOWER]
		
	elif char == "<TIM>":
		finalChar = [LETTER_CONSTANTS.TIMES.value - 1, LOWER]
			
	
	
	#Set Up the Letter Sprite
	if (finalChar[1] == LOWER):
	
		letterSprite.sprite_index = "spr_lowercase_letters"
	
	else:
	
		letterSprite.sprite_index = "spr_uppercase_letters"	
	
		
	letterSprite.image_index = finalChar[0]
	letterSprite.image_speed = 0

	
# Translate String
'''
	Translates a string into an array of letter indeces.
'''
def scrTranslateString(string):

	array_i = 0
	specialCharCount = 0
	
	#Get the Special Character Count
	for i in range(len(string)):
	
		if (string[i] == "<"):
		
			specialCharCount += 1
			
			i += 4
		
	
	
	#Denote the Size of the Final String
	finalString = array_create(len(string) - (4 * specialCharCount))
	
	#Add Each Letter
	for i in range(len(string)):
	
		currentChar = string[i]
		
		#Check for Special Characters
		if (currentChar == "<"):
		
			specialChar = string[i:i + 5]
			
			if specialChar == "<PK_>":
				finalString[array_i] = [LETTER_CONSTANTS.PK.value - 1, LOWER]
					
			elif specialChar == "<MN_>":
				finalString[array_i] = [LETTER_CONSTANTS.MN.value - 1, LOWER]
					
			elif specialChar == "<M__>":
				finalString[array_i] = [LETTER_CONSTANTS.MALE.value - 1, LOWER]
					
			elif specialChar == "<F__>":
				finalString[array_i] = [LETTER_CONSTANTS.FEMALE.value - 1, LOWER]
					
			elif specialChar == "<TIM>":
				finalString[array_i] = [LETTER_CONSTANTS.TIMES.value - 1, LOWER]
					
			
			
			#Skip the Additional Special Chars
			i += 4
		
		else:
		
			#Check the Standard Characters
			if currentChar == "a":
				finalString[array_i] = [LETTER_CONSTANTS.A.value - 1, LOWER]
				
			elif currentChar == "b":
				finalString[array_i] = [LETTER_CONSTANTS.B.value - 1, LOWER]
				
			elif currentChar == "c":
				finalString[array_i] = [LETTER_CONSTANTS.C.value - 1, LOWER]
				
			elif currentChar == "d":
				finalString[array_i] = [LETTER_CONSTANTS.D.value - 1, LOWER]
				
			elif currentChar == "e":
				finalString[array_i] = [LETTER_CONSTANTS.E.value - 1, LOWER]
				
			elif currentChar == "f":
				finalString[array_i] = [LETTER_CONSTANTS.F.value - 1, LOWER]
				
			elif currentChar == "g":
				finalString[array_i] = [LETTER_CONSTANTS.G.value - 1, LOWER]
				
			elif currentChar == "h":
				finalString[array_i] = [LETTER_CONSTANTS.H.value - 1, LOWER]
				
			elif currentChar == "i":
				finalString[array_i] = [LETTER_CONSTANTS.I.value - 1, LOWER]
				
			elif currentChar == "j":
				finalString[array_i] = [LETTER_CONSTANTS.J.value - 1, LOWER]
				
			elif currentChar == "k":
				finalString[array_i] = [LETTER_CONSTANTS.K.value - 1, LOWER]
				
			elif currentChar == "l":
				finalString[array_i] = [LETTER_CONSTANTS.L.value - 1, LOWER]
				
			elif currentChar == "m":
				finalString[array_i] = [LETTER_CONSTANTS.M.value - 1, LOWER]
				
			elif currentChar == "n":
				finalString[array_i] = [LETTER_CONSTANTS.N.value - 1, LOWER]
				
			elif currentChar == "o":
				finalString[array_i] = [LETTER_CONSTANTS.O.value - 1, LOWER]
				
			elif currentChar == "p":
				finalString[array_i] = [LETTER_CONSTANTS.P.value - 1, LOWER]
				
			elif currentChar == "q":
				finalString[array_i] = [LETTER_CONSTANTS.Q.value - 1, LOWER]
				
			elif currentChar == "r":
				finalString[array_i] = [LETTER_CONSTANTS.R.value - 1, LOWER]
				
			elif currentChar == "s":
				finalString[array_i] = [LETTER_CONSTANTS.S.value - 1, LOWER]
				
			elif currentChar == "t":
				finalString[array_i] = [LETTER_CONSTANTS.T.value - 1, LOWER]
				
			elif currentChar == "u":
				finalString[array_i] = [LETTER_CONSTANTS.U.value - 1, LOWER]
				
			elif currentChar == "v":
				finalString[array_i] = [LETTER_CONSTANTS.V.value - 1, LOWER]
				
			elif currentChar == "w":
				finalString[array_i] = [LETTER_CONSTANTS.W.value - 1, LOWER]
				
			elif currentChar == "x":
				finalString[array_i] = [LETTER_CONSTANTS.X.value - 1, LOWER]
				
			elif currentChar == "y":
				finalString[array_i] = [LETTER_CONSTANTS.Y.value - 1, LOWER]
				
			elif currentChar == "z":
				finalString[array_i] = [LETTER_CONSTANTS.Z.value - 1, LOWER]
				
			elif currentChar == "A":
				finalString[array_i] = [LETTER_CONSTANTS.A.value - 1, UPPER]
				
			elif currentChar == "B":
				finalString[array_i] = [LETTER_CONSTANTS.B.value - 1, UPPER]
				
			elif currentChar == "C":
				finalString[array_i] = [LETTER_CONSTANTS.C.value - 1, UPPER]
				
			elif currentChar == "D":
				finalString[array_i] = [LETTER_CONSTANTS.D.value - 1, UPPER]
				
			elif currentChar == "E":
				finalString[array_i] = [LETTER_CONSTANTS.E.value - 1, UPPER]
				
			elif currentChar == "F":
				finalString[array_i] = [LETTER_CONSTANTS.F.value - 1, UPPER]
				
			elif currentChar == "G":
				finalString[array_i] = [LETTER_CONSTANTS.G.value - 1, UPPER]
				
			elif currentChar == "H":
				finalString[array_i] = [LETTER_CONSTANTS.H.value - 1, UPPER]
				
			elif currentChar == "I":
				finalString[array_i] = [LETTER_CONSTANTS.I.value - 1, UPPER]
				
			elif currentChar == "J":
				finalString[array_i] = [LETTER_CONSTANTS.J.value - 1, UPPER]
				
			elif currentChar == "K":
				finalString[array_i] = [LETTER_CONSTANTS.K.value - 1, UPPER]
				
			elif currentChar == "L":
				finalString[array_i] = [LETTER_CONSTANTS.L.value - 1, UPPER]
				
			elif currentChar == "M":
				finalString[array_i] = [LETTER_CONSTANTS.M.value - 1, UPPER]
				
			elif currentChar == "N":
				finalString[array_i] = [LETTER_CONSTANTS.N.value - 1, UPPER]
				
			elif currentChar == "O":
				finalString[array_i] = [LETTER_CONSTANTS.O.value - 1, UPPER]
				
			elif currentChar == "P":
				finalString[array_i] = [LETTER_CONSTANTS.P.value - 1, UPPER]
				
			elif currentChar == "Q":
				finalString[array_i] = [LETTER_CONSTANTS.Q.value - 1, UPPER]
				
			elif currentChar == "R":
				finalString[array_i] = [LETTER_CONSTANTS.R.value - 1, UPPER]
				
			elif currentChar == "S":
				finalString[array_i] = [LETTER_CONSTANTS.S.value - 1, UPPER]
				
			elif currentChar == "T":
				finalString[array_i] = [LETTER_CONSTANTS.T.value - 1, UPPER]
				
			elif currentChar == "U":
				finalString[array_i] = [LETTER_CONSTANTS.U.value - 1, UPPER]
				
			elif currentChar == "V":
				finalString[array_i] = [LETTER_CONSTANTS.V.value - 1, UPPER]
				
			elif currentChar == "W":
				finalString[array_i] = [LETTER_CONSTANTS.W.value - 1, UPPER]
				
			elif currentChar == "X":
				finalString[array_i] = [LETTER_CONSTANTS.X.value - 1, UPPER]
				
			elif currentChar == "Y":
				finalString[array_i] = [LETTER_CONSTANTS.Y.value - 1, UPPER]
				
			elif currentChar == "Z":
				finalString[array_i] = [LETTER_CONSTANTS.Z.value - 1, UPPER]
				
			elif currentChar == "0":
				finalString[array_i] = [LETTER_CONSTANTS.ZERO.value - 1, LOWER]
				
			elif currentChar == "1":
				finalString[array_i] = [LETTER_CONSTANTS.ONE.value - 1, LOWER]
				
			elif currentChar == "2":
				finalString[array_i] = [LETTER_CONSTANTS.TWO.value - 1, LOWER]
				
			elif currentChar == "3":
				finalString[array_i] = [LETTER_CONSTANTS.THREE.value - 1, LOWER]
				
			elif currentChar == "4":
				finalString[array_i] = [LETTER_CONSTANTS.FOUR.value - 1, LOWER]
				
			elif currentChar == "5":
				finalString[array_i] = [LETTER_CONSTANTS.FIVE.value - 1, LOWER]
				
			elif currentChar == "6":
				finalString[array_i] = [LETTER_CONSTANTS.SIX.value - 1, LOWER]
				
			elif currentChar == "7":
				finalString[array_i] = [LETTER_CONSTANTS.SEVEN.value - 1, LOWER]
				
			elif currentChar == "8":
				finalString[array_i] = [LETTER_CONSTANTS.EIGHT.value - 1, LOWER]
				
			elif currentChar == "9":
				finalString[array_i] = [LETTER_CONSTANTS.NINE.value - 1, LOWER]
				
			elif currentChar == "-":
				finalString[array_i] = [LETTER_CONSTANTS.DASH.value - 1, LOWER]
				
			elif currentChar == "?":
				finalString[array_i] = [LETTER_CONSTANTS.QUESTION.value - 1, LOWER]
				
			elif currentChar == "!":
				finalString[array_i] = [LETTER_CONSTANTS.EXCLAMATION.value - 1, LOWER]
				
			elif currentChar == "(":
				finalString[array_i] = [LETTER_CONSTANTS.PAR_L.value - 1, LOWER]
				
			elif currentChar == ")":
				finalString[array_i] = [LETTER_CONSTANTS.PAR_R.value - 1, LOWER]
				
			elif currentChar == ":":
				finalString[array_i] = [LETTER_CONSTANTS.COLON.value - 1, LOWER]
				
			elif currentChar == "":
				finalString[array_i] = [LETTER_CONSTANTS.SEMICOLON.value - 1, LOWER]
				
			elif currentChar == "[":
				finalString[array_i] = [LETTER_CONSTANTS.BRAC_L.value - 1, LOWER]
				
			elif currentChar == "]":
				finalString[array_i] = [LETTER_CONSTANTS.BRAC_R.value - 1, LOWER]
				
			elif currentChar == "#":
				finalString[array_i] = [LETTER_CONSTANTS.BACKSLASH.value - 1, LOWER]
				
			elif currentChar == ".":
				finalString[array_i] = [LETTER_CONSTANTS.DOT.value - 1, LOWER]
				
			elif currentChar == ",":
				finalString[array_i] = [LETTER_CONSTANTS.COMMA.value - 1, LOWER]
				
			elif currentChar == "'":
				finalString[array_i] = [LETTER_CONSTANTS.APOSTROPHE.value - 1, LOWER]
				
			elif currentChar == " ":
				finalString[array_i] = [LETTER_CONSTANTS.SPACE.value - 1, LOWER]
				
			elif currentChar == "_":
				finalString[array_i] = [LETTER_CONSTANTS.UNDERSCORE.value - 1, LOWER]
				
			elif currentChar == "\n":
				finalString[array_i] = [LETTER_CONSTANTS.NEW_LINE.value - 1, LOWER]
			
					
			
		
		
		#Increment Our Final Array Position
		array_i += 1
	
	
	return finalString

	
