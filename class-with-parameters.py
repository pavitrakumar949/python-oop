class car:
	wheels=4

	def sample(self,brand,model,price,milage):
		self.brand = brand
		self.model = model
		self.price = price
		self.milage = milage		#these self.XXX are not class level variables
		print(brand,model,price,milage)	#this parameter is only accessible to this one method only not to the sample_two

	def sample_two(self):
		print(self.wheels)
		print(self.brand,self.model,self.milage,self.price)	#this will work

car1= car()
car1.sample('honda','Amaze',900000,14.5)
