class A:
	a=5
	def sample(self):
		print('Inside sample method of A')
class B(A):
	a=10
	def sample(self):
		print('Inside sample method of B')
obj=B()
print(obj.a)			#10 will be printed as a=5 will be overwritten
obj.sample()			#”Inside sample method of B” will be printed out
