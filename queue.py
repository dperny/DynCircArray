from dcarray import *

def testqueue():

    x = queue()
    operation = "h"
    FLAG = False
    i = 0

    while(operation != "q"):

        op = input("input operation: ")
        operation = operation if (op == "") else op

        if(operation == "_F"):
            FLAG = not FLAG
            continue

        elif(operation == "h"):
            print("Options: \n\teq to enqueue\n\tdq to dequeue")
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

        elif(operation == "dq"):
            try: print(x.dequeue())
            except SizeError: print("queue is empty")

        elif(operation == "pe"):
            try: print(x.peek())
            except IndexError: print("queue is empty")

        elif(operation == "eq"):
            if FLAG: datum = i; i += 1
            else: datum = eval(input("input datum: "))
            x.enqueue(datum)

        else:
            print("invalid option")

    return


class queue(object):
    """docstring for Queue"""
    def __init__(self):
        self._store = DCArray(4)
        self._size = 0

    def enqueue(self,value):
        self._store.backadd(value)
        self._size += 1

    def dequeue(self):
        if(self.isEmpty()):
            raise SizeError("stack is empty")
        self._size -= 1
        return self._store.frontremove()

    def peek(self):
        return self._store.get(0)

    def size(self):
        return self._size()

    def isEmpty(self):
        if(self._size == 0):
            return True
        else:
            return False

    def visualize(self):
        return self._store.extract()