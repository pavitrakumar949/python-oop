class A:
	a=9
	def method_a(self):
		print('inside method a')


class B(A):		#will inherit all the properties of class a
	b=10
	def method_b(self):
		print('inside method b')

obj = B()
print(obj.a)
print(obj.b)
obj.method_a()
obj.method_b()
