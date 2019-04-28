class Deque():
    
    def __init__(self):
       self.elements = []
       
    def Is_Empty(self):
        if not self.elements:
            return True
        else:
            return False

    def Insert_Left(self, value):
        self.elements.insert(0, value)

    def Insert_Right(self, value):
        self.elements.append(value)

    def Remove_Left(self):
        self.elements.pop(0)

    def Remove_Right(self):
        self.elements.pop()

    def Print_Deque(self):
        for i in self.elements:
            print("{0} ".format(i), end="")
        print("\n")


if __name__ == "__main__":
    import time
    start_time = time.time()
    deque = Deque()
    for i in range(0, 100000000):
        deque.Insert_Right(i)
    #deque.Print_Deque()
    print("--- %s seconds ---" % (time.time() - start_time))