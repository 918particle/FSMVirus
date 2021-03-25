#States: 00 - moving, 01 - eating, 10 - reproducing, 11 - dying
#Inputs: 0 - no food, 1 - food
#Outputs: 0 - dead, 1 - alive

class FSM:
	def __init__(self,x=0,y=0):
		self.current_state = '00'
		self.current_output = '1'
		self.pos_x = x
		self.pos_y = y
	def act(self,input):
		if(input == '0' and self.current_state == '00'):
			self.current_state = '11'
			self.current_output = '1'
		elif (input == '1' and self.current_state == '00'):
			self.current_state = '01'
			self.current_output = '1'
		elif (input == '0' and self.current_state == '01'):
			self.current_state = '00'
			self.current_output = '1'
		elif (input == '1' and self.current_state == '01'):
			self.current_state = '10'
			self.current_output = '1'
		elif (input == '0' and self.current_state == '10'):
			self.current_state = '00'
			self.current_output = '1'
		elif (input == '1' and self.current_state == '10'):
			self.current_state = '01'
			self.current_output = '1'
		elif (input == '0' and self.current_state == '11'):
			self.current_state = '11'
			self.current_output = '0'
		elif (input == '1' and self.current_state == '11'):
			self.current_state = '01'
			self.current_output = '1'
	def get_state(self):
		return self.current_state
	def get_output(self):
		return self.current_output
