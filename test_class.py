import os

class TestClass():
	def __init__(self, arg1, arg2):
		self.arg1 = arg1
		self.arg2 = arg2

	def method_1(self):
		return self.arg1 + self.arg2

	def method_2(self, arg3):
		if arg3:
			print("arg3 is {}".format(arg3))
			return 2*(self.arg1 + self.arg2)

def true_value():
	return False

def print_filepath():
	print(os.path.dirname(os.path.abspath(__file__)))
