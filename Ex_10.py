'''
Program to implement to see if an element is present in a stack using a queue
'''


class Stack_and_Queue:
	stack_capacity = 5


	def __init__(self):
		self.count = 0
		self.data = []*Stack_and_Queue.stack_capacity
		self.front = 0 	
		self.rear = 0
		self.size = 0


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


	def search(self,element):
		count_1 = 0 
		for i in range(self.count):
			x = self.pop()
			if x is not None:
				if x is not element:
					self.enqueue1(x)
					count_1 += 1
					self.count -= 1					
				else:
					print("Element is found in the position", self.count+1)
					self.deque1()





# The implementation that follows is regarding the Queues

	def enqueue1(self, item):
				
		next = (self.front + self.size)%len(self.data)
		self.data[next] = item
		self.size += 1
		self.rear += 1

# deque1 is implemented differently, made to behave like a stack here
	def deque1(self):
		if not self.is_empty():
			while self.size is not 0:
				element = self.data[self.rear-1]
				self.rear = (self.rear - 1)%len(self.data)
				self.size -= 1

				# Now the element is pushed back into the stack
				self.push(element)
		


Leaky = Stack_and_Queue()

for i in range(8):
	Leaky.push(i*3)

element = input('Enter the element to be searched for')
Leaky.search(element)

