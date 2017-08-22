'''
Designing a queue using two stacks as instance variables. One stack inside the class and one outside the class

'''

import sys

class Stack_and_Queue:
	stack_capacity = 5


	def __init__(self):
		self.count = 0
		
		self.data = [None]*Stack_and_Queue.stack_capacity
		self.size = 0
		
		
		
		


	def is_full(self):
		return Stack_and_Queue.stack_capacity == self.count


	def push(self, key):
		if not self.is_full():
			self.data[self.count] = key
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
data_1 = [None]*8
count_1 = 0


for i in range(5):
	Double.push(i*3)
print("Implementing deque using stack")

# Data popped from one stack is pushed into another stack

for i in range(5):
	item = Double.pop()
	data_1[count_1] = item
	count_1 += 1
for i in range(5):
	print(data_1[count_1-1])
	count_1 -= 1





