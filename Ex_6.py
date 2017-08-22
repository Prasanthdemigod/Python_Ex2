'''

Implementation of a program to perform operations on a stack

'''


class Leaky_stack:
	stack_capacity = 10


	def __init__(self):
		self.count = 0
		self.data_1 = []*Leaky_stack.stack_capacity
		self.front = 0 	
		self.data_2 = []*Leaky_stack.stack_capacity
		self.data_3 = []*Leaky_stack.stack_capacity


	def is_full(self):
		return Leaky_stack.stack_capacity == self.count


	def push_1(self, key):
		if not self.is_full():
			self.data_1.append(key)
			self.count += 1
			print("Item pushed in stack 1 is ", key)


		else:
			item_out = self.data_1[self.front]
			self.data_1[self.front] = None
			self.front = (self.front + 1)%len(self.data_1) # FRONT HAS TO BE INCREMENTED TO POINT TO THE NEW FIRST VALUE
			self.data_1.append(key)
			print("Now Item pushed in is", key)

	def push_2(self, key):
		if not self.is_full():
			self.data_2.append(key)
			self.count += 1
			print("Item pushed in stack 2 is ", key)


		else:
			item_out = self.data_2[self.front]
			self.data_2[self.front] = None
			self.front = (self.front + 1)%len(self.data_2) # FRONT HAS TO BE INCREMENTED TO POINT TO THE NEW FIRST VALUE
			self.data_2.append(key)
			print("Now Item pushed in is", key)

	def push_3(self, key):
		if not self.is_full():
			self.data_3.append(key)
			self.count += 1
			print("Item pushed in stack 3 is ", key)


		else:
			item_out = self.data_1[self.front]
			self.data_3[self.front] = None
			self.front = (self.front + 1)%len(self.data_3) # FRONT HAS TO BE INCREMENTED TO POINT TO THE NEW FIRST VALUE
			self.data_3.append(key)
			print("Now Item pushed in is", key)



	def is_empty(self):
		return self.count == 0

	def pop_1(self):
		if not self.is_empty():
			self.count -= 1
			return self.data_1.pop()


	def pop_2(self):
		if not self.is_empty():
			self.count -= 1
			return self.data_2.pop()

	def pop_3(self):
		if not self.is_empty():
			self.count -= 1
			return self.data_3.pop()

	def peek(self):
		if not self.is_empty():
			return self.data[-1]




Leaky = Leaky_stack()

for i in range(4):
	Leaky.push_1(i)

for i in range(6,10):
	Leaky.push_2(i)

for i in range(4,6):
	Leaky.push_3(i)

for i in range(2):
	item = Leaky.pop_3()
	Leaky.push_1(item)

for i in range(2):
	item = Leaky.pop_1()
	Leaky.push_2(item)

print("\n Items in stack2 now include")

for i in range(6):
	print(Leaky.pop_2())
