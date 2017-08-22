'''
Designing a double eneded queue using two stacks as instance variables

'''

import sys

class Stack_and_Queue:
	stack_capacity = 8


	def __init__(self):
		self.count = 0
		self.data = [None]*Stack_and_Queue.stack_capacity
		self.front = 0 	
		self.rear = 0
		self.size = 0
		self.size_1 = 0
		self.top_1 = 0
		self.data_1 = [None]*Stack_and_Queue.stack_capacity
		self.size_2 = 0


	def is_full(self):
		return Stack_and_Queue.stack_capacity == self.count


	def push(self, key):
		if not self.is_full():
			self.data.append(key)
			print("Item pushed at index ",self.count," is ", key)
			self.count += 1

		
	def is_empty(self):
		return self.count == 0

	def pop(self):
		if not self.is_empty():
			self.count -= 1
			return self.data.pop()

	def peek(self):
		if not self.is_empty():
			return self.data[-1]


	def addFront(self):
		item = input("Enter the item ")
		for i in range(self.size):
			temp = self.deque1()
			self.data_1[self.top_1] = temp
			self.size_1 += 1
			self.top_1 += 1
		self.data[self.top_1] = item
		self.size_1 += 1
		self.top_1 += 1
		
		print("Displaying the queue implemented using stack for Add front ", self.data)

	def addRear(self):
		item = input("Enter the item ")
		self.addFront()
		self.top_1 = 0

		for i in range(self.size_1):
			self.data_1[self.top_1] = self.data_1.pop()
			self.top_1 += 1
			self.size_2 += 1

		print("data_1 is: ",self.data_1)

		self.data_1[self.top_1] = item
		print("data_1 is", self.data_1)

		for i in range(self.size_2):
			item = self.data_1.pop()
			print(item)
			self.enqueue1(item)

		self.display()


	def addRear(self):
		item = input("Enter the item ")
		self.data.insert(0,item)

	def removeFront(self):
		print(self.data.pop())

	def removeRear(self):
		print(self.data.pop(0))

	def display(self):
		print(self.data)



	

# The implementation that follows is regarding the Queues

	def enqueue1(self, item):
				
		next = (self.front + self.size)%len(self.data)
		self.data[next] = item
		self.size += 1


# deque1 is implemented differently, made to behave like a stack here
	def deque1(self):
		if not self.is_empty():
			element = self.data[self.front]
			self.data[self.front] = None
			self.front = (self.front + 1)%len(self.data)
			self.size -= 1
			return element



Double = Stack_and_Queue()

for i in range(5):
	Double.enqueue1(i*3)

print("The Queue list is :", Double.data)

for i in range(7):
	num = input("What do you want to do: 1:Enqueue 2: Dequeue 3: Add Front 4: Add End 5:Delete front 6: Delete back 7:Display")
	options = {
			   3 : Double.addFront,
			   4 : Double.addRear,
			   5 : Double.removeFront,
			   6 : Double.removeRear,           

	}

	options[num]()	

