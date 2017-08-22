'''
Implementing stack using a single queue and an additional memory

'''


import sys

class Stack_and_Queue:
	stack_capacity = 5


	def __init__(self):
		self.count = 0
		
		self.data = [None]*Stack_and_Queue.stack_capacity
		self.size = 0
		self.rear = 0	
		self.front = 0
		
		


	def is_full(self):
		return Stack_and_Queue.stack_capacity == self.count


	def enque(self, key):
		if not self.is_full():
			self.data[self.rear] = key
			print("Item pushed at index ",self.count," is ", key)
			self.rear += 1
			self.count += 1


	
	def is_empty(self):
		return self.count == 0

	def deque(self):
		
		
		if not self.is_empty():
			
			while i is not self.rear:
				print(self.data[self.rear-1])
				self.rear -= 1		


			
	def peek(self):
		if not self.is_empty():
			return self.data[-1]


	

	def addRear(self):
		item = input("Enter the item ")
		self.data.insert(0,item)

	def removeFront(self):
		print(self.data.pop())

	def removeRear(self):
		print(self.data.pop(0))

	def display(self):
		print(self.data)



Double = Stack_and_Queue()

for i in range(5):
	Double.enque(i*3)

print("Popping now")
#for i in range(5):
Double.deque()







