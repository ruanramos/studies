class Queue:
	
	def __init__(self):
		self.elements = []


	def Is_Empty(self):
		if not self.elements:
			return True
		return False

	def Enqueue(self, element):
		self.elements.append(element)
		return self.elements[-1]
		# preciso checar caso de lista estar cheia?

	def Dequeue(self):
		if not self.Is_Empty():
			return self.elements.pop(0)
		return False

	def Print(self):
		for i in self.elements:
			print(str(i) + " ", end="")
		print("\n")


if __name__ == "__main__":
	queue = Queue()
	queue.Print()
	print("---------------")
	queue.Enqueue(10)
	queue.Enqueue(20)
	queue.Enqueue(30)
	queue.Enqueue(40)
	queue.Enqueue(50)
	queue.Print()
	print("------------")
	queue.Dequeue()
	queue.Dequeue()
	queue.Dequeue()
	queue.Print()
	print("------------")