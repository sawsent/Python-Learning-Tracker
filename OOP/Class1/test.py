class MyClass:
	def __init__(self, name):
		self.__name = name
	
	@property
	def name(self):
		return self.__name

test_inst = MyClass("test")

test_inst.__name = "something else"

print(test_inst.__name)
print(test_inst.name)