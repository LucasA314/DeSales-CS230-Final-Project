import core

class obj_letter(core.Object):
	def __init__(self, main):
		core.Object.__init__(self, main, "spr_lowercase_letters", 56, True)
	
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