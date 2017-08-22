'''

Program to implement push opeartion from one stack to another stack 

'''

import sys

class LimitedStack:
	Stack_capacity = 10
	
	def __init__(self):
		self.count = 0
		self.data = [None]*LimitedStack.Stack_capacity

	def isfull(self):
		return LimitedStack.Stack_capacity == self.count

	def push(self, key):
		tryif not self.isfull():
			self.data[self.count] = key
			self.count += 1
		else:
			print("stack is full")


	def isempty(self):
		return self.count == 0

	def pop(self):
		if not self.isempty():
			self.count -= 1
			return self.data.pop()

	def length(self):
		return self.count

	def peek(self):
		if not self.isempty():
			return self.data[-1]


stack = LimitedStack()


print("Stack 1:")

for i in range(13):
	stack.push(i)


	




