class car:
	wheels=4
	def start_car(self): 	#self is by default used in python for a method
		print('car started')

	def example_one(self):
		print(self.wheels)	#wheels alone will not work we will have to include the word self.
		self.start_car()		#will also work as we can access the other method

car1=car()
print(car1.wheels)
car1.start_car()
