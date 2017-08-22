'''

A program to implement a leaky stack 

'''


class Leaky_stack:
	stack_capacity = 5


	def __init__(self):
		self.count = 0
		self.data = []*Leaky_stack.stack_capacity
		self.front = 0 	

	def is_full(self):
		return Leaky_stack.stack_capacity == self.count


	def push(self, key):
		if not self.is_full():
			self.data.append(key)
			self.count += 1
			print("Item pushed is ", key)


		else:
			item_out = self.data[self.front]
			self.data[self.front] = None
			self.front = (self.front + 1)%len(self.data) # FRONT HAS TO BE INCREMENTED TO POINT TO THE NEW FIRST VALUE
			self.data.append(key)
			print("Item pushed out is :", item_out)
			print("Now Item pushed in is", key)

	def is_empty(self):
		return self.count == 0

	def pop(self):
		if not self.is_empty():
			self.count -= 1
			return self.data.pop()

	def peek(self):
		if not self.is_empty():
			return self.data[-1]




Leaky = Leaky_stack()

for i in range(8):
	Leaky.push(i)

