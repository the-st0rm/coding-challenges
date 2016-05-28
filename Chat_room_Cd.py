#!/usr/bin/env python
#ahhellllloou
target = 'hello'
Input = raw_input()
counter = 0
L  =len(Input)
L2 = len(target)
cursor = 0
while counter < L and cursor < L2:
    if Input[counter]==target[cursor]:
        cursor+=1
    #elif Input[counter]!=target[cursor-1]:
    #    cursor = 0
    #    if Input[counter]==target[cursor]:
    #        cursor+=1
    counter +=1

if cursor==L2:
    print 'YES'
else:
    print 'NO'
