# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:44:04 2022

@author: lucas
"""


import core

class obj_letter(core.Object):
	def __init__(self):
		core.Object.__init__(self, "spr_lowercase_letters", 56, True)
	
	def create(self, main):
		#Freeze
		self.image_speed = 0
		self.eliminate = False
		
		return main
	
	def update(self, main):
		#Delete
		if self.eliminate:
			core.instance_destroy(main, self)	
		
		return main