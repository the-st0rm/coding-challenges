#!/usr/bin/env python
import os
class stack:
    ll = None
    cursor = -1
    MAX_SIZE = 10
    def __init__(self, size=10):
        self.MAX_SIZE = size
        self.ll = [None]*size
        self.cursor = -1
        
    def pop(self):
        if self.cursor ==-1:
            print "ERROR STACK UNDERFLOW"
            return -1
        output = self.ll[self.cursor]
        self.cursor-=1
        return output
    def push(self, val):
        if self.cursor+1 >= self.MAX_SIZE:
            print "ERROR STACK OVERFLOW"
            return -1
        else:
            self.cursor+=1
            self.ll[self.cursor]=val
            return 1
        

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print BASE_DIR
s = stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.pop()
print s.pop()