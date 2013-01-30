from dcarray import *

class stack(object):
    """docstring for stack"""
    def __init__(self):
        self._store = DCArray(4)
        self._size = 0
    
    def push(self,value):
        self._store.frontadd(value)
        size =+ 1

    def pop(self):
        if(self.isEmpty())
            return SizeError("stack is empty")
        self._size -= 1
        return self._store.frontremove()

    def peek(self):
        return self._store.get(size-1)

    def size(self):
        return self._size

    def isEmpty(self):
        if(self._size == 0):
            return True
        else:
            return False

    def visualize(self):
        return self.store.extract()