def testdcarray():

    size = input("input the size of the dynamic circular array: ")
    x = DCArray(int(size))

    #options block. shows commands

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

        elif(operation == "si"):
            print("size of the array is {0}".format(x.size()))
            continue

        elif(operation == "raw"):
            print(x.display)

        # datum is i (increment i each time) if sequential mode is on
        # else get user input
        if FLAG: datum = i; i += 1
        else: datum = input("input datum: ")

        if(operation == "s"):
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

class DCArray:
    """A class for a circular arrays in python.

    takes the array capacity as an argument

    front, back, and positional insertions and deletions supported
    also supports isEmpty and isFull

    """

    def __init__(self,capacity):
        self._store = [0] * capacity
        self._capacity = capacity
        self._factor = 2
        self._size = 0
        self._startIndex = 0
        self._endIndex = 0

    def get(self,index):
        """returns the value at index"""
        self._verifyIndex(index)
        return self._store[self._correct(self._startIndex + index)]

    def set(self,index,value):
        """sets the value at index"""
        self._verifyIndex(index)
        # store in the corrected index of the input the value
        self._store[self._correct(self._startIndex + index)] = value

    def frontadd(self,value):
        """adds value to the front of the array"""
        if(self.isFull() == True):
            self._grow()
        self._startIndex = self._correct(self._startIndex - 1)
        self._store[self._startIndex] = value
        self._size += 1

    def backadd(self,value):
        """adds a value to the back of the array"""
        if(self.isFull() == True):
            self._grow()
        self._store[self._endIndex] = value
        self._endIndex = self._correct(self._endIndex + 1)
        self._size += 1

    def frontremove(self):
        """removes and returns the frontmost value"""

        if(self.isEmpty() == True):
            raise SizeError("array is empty")
        elif(self._size <= self._capacity/4):
            self._shrink() 

        rval = self._store[self._startIndex]
        self._store[self._startIndex] = 0
        self._startIndex = self._correct(self._startIndex + 1)
        self._size -= 1
        return rval

    def backremove(self):
        """removes and returns the rearmost value"""

        if(self.isEmpty() == True):
            raise SizeError("array is empty")
        elif(self._size <= self._capacity/4):
            self._shrink()

        rval = self._store[self._correct(self._endIndex-1)]
        self._store[self._correct(self._endIndex - 1)] = 0
        self._endIndex = self._correct(self._endIndex - 1)
        self._size -= 1
        return rval

    def indexremove(self,index):
        """removes and returns the value at index"""
        if(self.isEmpty() == True):
            raise SizeError("array is empty")
        elif(self._size <= self._capacity/4):
            self._shrink()

        self._verifyIndex(index)
        rval = self.get(index)
        self.set(index,0)
        for i in range(index,self._size-1,1):
            self.set(i,self.get(i+1))
        i = index
        self._size -= 1
        self._endIndex = self._correct(self._endIndex - 1)
        return rval

    def extract(self):
        """returns a regular array with the contents in logical positions"""
        rlist = [0] * self._size
        for i in range(self._size):
            #use internal functions to make things easier, ya dingus
            rlist[i] = self.get(i) 
        return rlist

    def isEmpty(self):
        if(self._size <= 0):
            return True
        else:
            return False

    def isFull(self):
        if(self._size >= self._capacity):
            return True
        else:
            return False

    def size(self):
        """returns the size of the array. DAT ABSTRACTION"""
        return self._size

    def capacity(self):
        """returns the capacity of the array"""
        return self._capacity

    def display(self):
        return self._store

    #######################################################
    #            private functions below here             #
    #        GO AWAY THERE ARE NO EASTER EGGS HERE        #
    #######################################################

    # GOD I LOVE MODULAR ARITHMETIC.
    def _correct(self,index):
        return index % self._capacity

    # verifies that the index provided is valid
    def _verifyIndex(self,index):
        if(type(index) != int):
            raise TypeError("index must be of type int")
        elif(index > self._size-1):
            raise IndexError("index out of bounds")
        else:
            return

    def _grow(self):
        newstore = [0] * (self._capacity * self._factor)
        for i in range(self._size+1):
            newstore[i] = self._store[self._correct(i+self._startIndex)]

        self._store = newstore
        self._capacity = self._capacity * self._factor
        self._startIndex = 0
        self._endIndex = self._size

    def _shrink(self):
        newstore = [0] * (self._capacity // self._factor)
        for i in range(self._size):
            newstore[i] = self._store[self._correct(i+self._startIndex)]

        self._store = newstore
        self._startIndex = 0
        self._endIndex = self._size

        self._capacity = (self._capacity // self._factor)

class SizeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)