
class car:
	def __init__(self,brand,model,price,milage):
		self.brand=brand
		self.model=model
		self.price=price
		self.milage=milage

	def start_car(self):
		print(self.brand+' car is having model as '+self.model+ ' has started')

	def stop_car(self):
		print(self.brand+' car is having model as '+self.model+ ' has stopped')

	def print_car_details(self):
		print('brand of the car is: '+ self.brand)
		print('model of the car is: '+ self.model)
		print('price of the car is: '+ str(self.price))
		print('milage of the car is: '+ str(self.milage))

svdi=car('maruti','swift VDI', 80000,24)
hmz=car('honda','Amaze', 90000,14)

svdi.start_car()			#first data will be started
svdi.stop_car()
svdi.print_car_details()

hmz.start_car()			#second data will be started
hmz.stop_car()
hmz.print_car_details()
