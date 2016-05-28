#!/usr/bin/env python
#http://codeforces.com/problemset/problem/133/A
arr = [72, 81, 57]

Input = raw_input()
flag = 0
for l in Input:
    if ord(l) in arr:
        flag +=1

if flag >0:
    print 'YES'
else:
    print 'NO'
