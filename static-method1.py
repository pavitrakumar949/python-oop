class car:
	wheels = 4

	def __init__(self,brand,model,price,milage):
		self.brand=brand
		self.model=model
		self.price=price
		self.milage=milage

	def start_car(self):
		print(self.brand+ 'car having model as ' +self.model+' has started')

@staticmethod
def print_car_wheels():
 print(car.wheels)

svdi=car('maruti','Swift VDI',800000,4)
hmz=car('honda','Amaze',900000,14.5)

print(svdi.brand)
print(svdi.model)
print(svdi.price)
print(svdi.milage)
print(car.wheels)

svdi.start_car()
