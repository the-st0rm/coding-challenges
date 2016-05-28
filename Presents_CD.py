#!/usr/bin/env python
#http://codeforces.com/problemset/problem/136/A
L = input()
gift_arrays = map(int, raw_input().split(' '))
givers = [0]*L
for i in gift_arrays:
    givers[i-1]=gift_arrays.index(i)+1
    
print str(givers).strip('[]').replace(',', '')
