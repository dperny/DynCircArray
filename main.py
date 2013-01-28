from dcarray import *

def main():

	print("This is the data structures testing tool")
	size = input("input the size of the data structure: ")
	x = DCArray(int(size))

	#options block. shows commands

	operation = "h"
	FLAG = False
	i = 0

	while(operation != "q"):

		op = input("input operation: ")
		operation = operation if op == "r" else op

		if(operation == "_F"):
			FLAG = not FLAG
			continue

		elif(operation == "h"):
			print("Options: \n\tg to get at index \n\ts to set at index")
			print("\tba to add to back\n\tfa to add to front")
			print("\tbr to remove from back\n\tfr to remove from front")
			print("\tir to remove from index\n\te to extract")
			print("\tie for isEmpty\n\tif for isFull")
			print("\tsi for size\n\traw to view raw store\n\tr for repeat last command")
			print("\t_F to toggle sequential (quick) data\n\tq to quit")
			continue

		elif(operation == "g"): 
			index = int(input("index: "))

			try:
				rval = x.get(index)
			except IndexError:
				print("index is out of bounds")
				continue

			print("index {0} is {1}".format(index,rval))
			continue

		elif(operation == "fr"):
			print("value {0} was removed from the front".format(x.frontremove()))
			continue

		elif(operation == "br"):
			print("value {0} was removed from the back".format(x.backremove()))
			continue

		elif(operation == "ir"): 
			index = int(input("index: "))
			try:
				print("value {0} was removed from index{1}".format(x.indexremove(index),index))
			except IndexError:
				print("invalid index")
			continue

		elif(operation == "e"):
			print(x.extract())
			continue

		elif(operation == "ie"):
			print("array is empty") if x.isEmpty() else print("array not empty")
			continue

		elif(operation == "if"):
			print("array is full") if x.isFull() else print("array not full")
			continue

		elif(operation == "s"):
			print("size of the array is {0}".format(x.size()))
			continue

		# datum is i (increment i each time) if sequential mode is on
		# else get user input
		if FLAG: datum = i; i += 1
		else: datum = input("input datum: ")

		if(operation == "si"):
			index = int(input("index: "))
			try:
				x.set(index,datum)
			except IndexError:
				print("index is out of bounds")
				continue

		elif(operation == "ba"):
			x.backadd(datum)
		elif(operation == "fa"):
			x.frontadd(datum)
		else:
			print("invalid option")
			

	
	return

main()