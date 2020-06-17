class Vaccine():
	
	def __init__(self,positionData):
		self.positionSet = set()
		for l in positionData:
			self.positionSet.add(l)

	def is_vaccinated(self,posx=0,posy=0):
		return ((posx,posy) in self.positionSet)