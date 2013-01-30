from dcarray import *

def teststack():

    x = stack()
    operation = "h"
    FLAG = False
    i = 0

    while(operation != "q"):

        op = input("input operation: ")
        operation = operation if (op == "r" or "") else op

        if(operation == "_F"):
            FLAG = not FLAG
            continue

        elif(operation == "h"):
            print("Options: \n\tpu to push\n\tpo to pop")
            print("\tp to peek \n\ts for size")
            print("\tie for isEmpty\n\tv for visualize")
            print("\t_F to toggle sequential (quick) add")
            print("\tq to quit")
            continue

        elif(operation == "ie"):
            print(x.isEmpty())
            continue

        elif(operation == "s"):
            print(x.size())
            continue

        elif(operation == "v"):
            print(x.visualize())
            continue

        elif(operation == "po"):
            try: print(x.pop())
            except SizeError: print("stack is empty")

        elif(operation == "pe"):
            try: print(x.peek())
            except SizeError: print("stack is empty")

        elif(operation == "pu"):
            if FLAG: datum = i; i += 1
            else: datum = input("input datum: ")
            x.push(datum)

        else:
            print("invalid option")

    return

class stack(object):
    """docstring for stack"""
    def __init__(self):
        self._store = DCArray(4)
        self._size = 0
    
    def push(self,value):
        self._store.frontadd(value)
        self._size += 1

    def pop(self):
        if(self.isEmpty()):
            return SizeError("stack is empty")
        self._size -= 1
        return self._store.frontremove()

    def peek(self):
        return self._store.get(self._size-1)

    def size(self):
        return self._size

    def isEmpty(self):
        if(self._size == 0):
            return True
        else:
            return False

    def visualize(self):
        return self._store.extract()