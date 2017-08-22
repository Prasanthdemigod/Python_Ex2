'''
This program illustrates the functioning of the Double Ended Queue

'''

import sys


class Double_Queue:

	default_capacity = 3


	def __init__(self):
		self.size=0
		self.front = 0
		self.rear = 0
		self.data = [None]*Double_Queue.default_capacity


	def addFront(self):
		item = input("Enter the item")
		self.data.append(item)

	def addRear(self, item):
		item = input("Enter the item")
		self.data.insert(0,item)

	def removeFront(self):
		print(self.data.pop())

	def removeRear(self):
		print(self.data.pop(0))


	def enqueue1(self):
		
		print("self.data size is:", len(self.data))	
		next = (self.front + self.size)%len(self.data)
		item = input("Input the Item to be added")
		self.data[next] = item
		self.size += 1


	def deque1(self):
		if not self.is_empty():
			element = self.data[self.front]
			self.data[self.front] = None
			self.front = (self.front + 1)%len(self.data)
			self.size -= 1
			return element

	def display(self):
		print(self.data)


	def is_empty(self):
		return self.size == 0

	def length(self):
		return self.size

	

Double = Double_Queue()



for i in range(7):
	num = input("What do you want to do: 1:Enqueue 2: Dequeue 3: Add Front 4: Add End 5:Delete front 6: Delete back 7:Display")
	
	options = {
			   1 : Double.enqueue1,
			   2 : Double.deque1,
			   3 : Double.addFront,
			   4 : Double.addRear,
			   5 : Double.removeFront,
			   6 : Double.removeRear,           
			   7 : Double.display, 
	}

	options[num]()	