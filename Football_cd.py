#!/usr/bin/env python
#http://codeforces.com/problemset/problem/96/A
Input = map(int, raw_input())
Dan = 1
counter = 1
Len = len(Input)
while counter < Len: 
    if Input[counter]==Input[counter-1]:
        Dan +=1
    else:
        Dan = 1
    if Dan == 7:
        counter = Len
    counter +=1
if Dan == 7:
    print "YES"
else:
    print "NO"
