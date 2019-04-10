class Stack:
	
	def __init__(self):
		self.elements = []


	def Is_Empty(self):
		if not self.elements:
			return True
		return False

	def Push(self, element):
		self.elements.append(element)
		return self.elements[-1]
		# preciso checar caso de lista estar cheia?

	def Pop(self):
		if not self.Is_Empty():
			return self.elements.pop()
		return False

	def Print(self):
		for i in self.elements[::-1]:
			print(i)


if __name__ == "__main__":
	stack = Stack()
	stack.Print()
	stack.Push(30)
	stack.Push(40)
	stack.Push(10)
	stack.Push(15)
	stack.Print()
	print("_________")
	stack.Pop()
	stack.Pop()
	stack.Print()