'''
This program illustrates the finding the total capital gain or loss in buying and selling of the stock prices based on the FIFO protocol to identify shares

'''

import sys


class CommonStock:

	default_capacity = 4


	def __init__(self):
		self.size=0
		self.front=0
		self.data = [None]*CommonStock.default_capacity


	def capital_calc(self):

		sum = 0

		N = input('Enter the number of transactions: ')

		for i in range(N):
			print 'Shares sold on day',i
			shares = input(':')
			price = input('price of the share')
			self.enqueue1(shares)
			self.enqueue2(price)

		sell_shares = input('Enter the no. of selling shares')
		sell_price = input('Enter the price for the selling share')

		temp = sell_shares
				
		for j in range(N):
			item_share = self.deque1()
			item_price = self.deque2()
			if item_share < temp:
				sum  += item_share*(sell_price - item_price)
				temp = temp - item_share

			else:
				sum += temp*(sell_price - item_price)


		return sum


	def enqueue1(self, shares):
		if self.size == len(self.data):
			self.resize(2*len(self.data))

		print("self.data size is:", len(self.data))	
		next = (self.front + self.size)%len(self.data)
		self.data[next] = shares
		self.size += 1


	def deque1(self):
		if not self.is_empty():
			element = self.data[self.front]
			self.data[self.front] = None

			self.front = (self.front + 1)%len(self.data)
			self.size -= 1
			return element


	def enqueue2(self, shares):
		if self.size == len(self.data):
			self.resize(2*len(self.data))

		next = (self.front + self.size)%len(self.data)
		self.data[next] = shares
		self.size += 1



	def deque2(self):
		if not self.is_empty():
			element = self.data[self.front]
			self.data[self.front] = None
			self.front = (self.front + 1)%len(self.data)
			self.size -= 1
			return element


	def is_empty(self):
		return self.size == 0

	def length(self):
		return self.size


	def resize(self, capacity):
		old = self.data
		walk = self.front
		self.data = [None]*capacity

		for k in range(len(old)):
			self.data[k] = old[walk]
			walk = (walk + 1)%len(old)

		self.front = 0



Common = CommonStock()
stock_value = Common.capital_calc()

print("The stock_value at the end of day 4 is ", stock_value)
