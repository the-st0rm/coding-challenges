#!/usr/bin/env python
#http://codeforces.com/problemset/problem/175/A
def get_max(num):
    maxes = list()
    counter =0
    L = len(num)
    while counter < L-1:    
        maxes.append(int(num[counter:counter+2])+int(num[(counter+2)%L])+int(num[(counter+3)%L]))
        counter+=1
    
    
    Max = max(maxes)
    if Max==0:
        return 0
    i = maxes.index(Max)
    if num[i]=='0':
        return -1
    return Max
    
print get_max(raw_input())
