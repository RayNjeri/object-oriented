class animal(object):
	def __init__(self,sound,number_of_legs,habitation,domestication):
		"""return a new animal object"""
		self.sound = sound
		self.number_of_legs = number_of_legs
		self.habitation = habitation
		self.domestication = domestication

	def sound(self, sound,habitation,domestication,number_of_legs):
		print("i %s,%s,%s,%d" (sound,habitation,domestication,number_of_legs))

	class cow:
		def sound(self):
			print(mooooooow)

		def habitation(self):
			print(ranch)

		def domestication(self):
			print(domestic)	

		def number_of_legs(self):
			print(4)

	class lion:
		def sound(self):		
			print(roars)

		def habitation(self):
			print(zoo)

		def domestication(self):
			print(wild)	

		def number_of_legs(self):
			print(4)

	class duck:
		def sound(self):		
			print(quacks)

		def habitation(self):
			print(water)

		def domestication(self):
			print(domestic)	

		def number_of_legs(self):
			print(2)

