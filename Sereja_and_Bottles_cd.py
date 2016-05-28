#!/usr/bin/env python
#http://codeforces.com/problemset/problem/315/A
n = input()
alphanum = '0123456789abcdefABCDEF'

def to_base(num, base):
    res = ''
    while num >0:
        
bottels = list()
for i in range(n):
    a, b = raw_input().split(' ')
    bottels.append((a, b, i))

res = n
for i in range(n):
    b = bottels[i]
    j =0
    while j < n:
        if j != i:
            if bottels[j][1]==b[0]:
                res -=1
                j = n
        j+=1
print res
