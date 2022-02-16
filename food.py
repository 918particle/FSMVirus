#States: 1 corresponds to healthy, 0 is infected

class Food:
	def __init__(self,x=0,y=0):
		self.current_state = '1'
		self.pos_x = x
		self.pos_y = y
		self.shot = False
	def get_state(self):
		return self.current_state
	def toggle_state(self):
		if(self.current_state == '1'):
			self.current_state = '0'
		else:
			self.current_state = '1'
	def vaccinate(self):
		self.shot = True
	def is_vaccinated(self):
		return self.shot
