class Animal(object):
	def __init__(self,name,sound,number_of_legs,habitation):
		"""return a new animal object"""
		self.name = name
		self.sound = sound
		self.number_of_legs = number_of_legs
		self.habitation = habitation
		

#inheritance

class Pet(Animal):
	def __init__(self,name,sound,number_of_legs,habitation,domestication,sleep):
		super().__init__(name,sound,number_of_legs,habitation)
		self.domestication = domestication
		self.sleep = sleep
		#print ( "i %s,%d,%s,%s,%S,%s"(name,sound,number_of_legs,habitation,domestication,sleep))
	def print_attributes(self):
		print (c.name)
		print (c.sound)
		print (c.number_of_legs)
		print (c.habitation)
		print (c.domestication)
		print (c.sleep)



class Wild(Animal):
	def __init__(self,name,sound,number_of_legs,habitation,prey,sleep):
		super().__init__(name,sound,number_of_legs,habitation)
		self.prey = prey
		self.sleep = sleep
		#print ( "i %s,%d,%s,%s,%S,%s"(name,sound,number_of_legs,habitation,prey,predator))
	def print_attributes(self):
		print (y.name)
		print (y.sound)
		print (y.number_of_legs)
		print (y.habitation)
		print (y.prey)
		print (y.sleep)		

c = Pet("dog","bark","4","kenel","domestic","zzz")

c.print_attributes()

y = Wild("lion","roar","4","zoo","prey","zzz")

y.print_attributes()