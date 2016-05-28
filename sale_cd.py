#!/usr/bin/env python
#http://codeforces.com/problemset/problem/34/B
n, m = map(int, raw_input().split(' '))
tvs = map(int, raw_input().split(' '))
tvs.sort()
res = 0
counter = 0 
while counter < m:
    num = -1 * tvs.pop(0)
    if num < 0:
        counter = m
    else:
        res += num
        counter +=1

print res
