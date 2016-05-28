#!/usr/bin/env python
#http://codeforces.com/problemset/problem/109/A
num = input()
if num%7 == 4:
    print '4'*((num-7)/4)+str('7')
else:
    print -1
