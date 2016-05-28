#!/usr/bin/env python
#http://codeforces.com/problemset/problem/3/A
s = raw_input()
t = raw_input()

pos = ['a','b','c','d','e','f','g','h']
source = (pos.index(s[0])+1, int(s[1]))
target = (pos.index(t[0])+1, int(t[1]))
print source
print target

curr = ['', source]
while True:
    right_m = curr[1][0]+1
    left_m = curr[1][0]-1
    up_m = curr[1][1]+1
    down = curr[1][1]-1
    
    if curr[1][0]+1<9 and curr[1][0]+2>0:
        
