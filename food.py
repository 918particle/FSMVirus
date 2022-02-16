class Food:
	def __init__(self,x=0,y=0):
		self.current_state = '1'
		self.pos_x = x
		self.pos_y = y
    def get_state(self):
        return self.current_state
