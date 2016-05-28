#!/usr/bin/env python

number = raw_input()

l = len(number)
s = 0
res = 0
while l >1:
    s=0
    for i in number:
        s+=int(i)
    number = str(s)
    l = len(number)
    res+=1
print res
