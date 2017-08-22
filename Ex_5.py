'''
To implement a program that parses a program with HTML tags, with attributes too

'''

import sys
import Stacks

def html_tags(raw_code):
	stk = Stacks.LimitedStack()
	j = raw_code.find('<')

	while j != -1:
		k = raw_code.find('>', j+1)
		if k == -1:
			return False

		tag = raw_code[j+1:k]
		if not tag.startswith('/'):
			lst = tag.split()   # splits if the tag has attributes
			stk.push(lst[0]) # pushes the first word which is generally the tag name 
			print("The word pushed is ", lst[0])

		else:
			if stk.isempty():
				return False


			if tag[1:] != stk.pop():
				return False

			
		j = raw_code.find('<', j+1)


	return stk.isempty()


File_data = open(sys.argv[1]).read()
print(File_data)


html_tags(File_data)

