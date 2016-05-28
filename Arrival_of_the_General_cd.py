#!/usr/bin/env python
#http://codeforces.com/problemset/problem/144/A

n = input();sold = map(int, raw_input().split(' '))
index_max = sold.index(max(sold))
index_min = n-sold[::-1].index(min(sold))-1
sol = index_max + (n-1)-index_min
if index_max > index_min:
    sol-=1
print sol
