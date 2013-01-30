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
        self._size -= 1
        return self._store.frontremove()

    def peek(self):
        return self._store.get(size-1)

    def size(self):
        return self._size

    def visualize(self):
        return self.store.extract()