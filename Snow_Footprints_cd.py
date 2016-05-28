#!/usr/bin/env python
#http://codeforces.com/problemset/problem/298/A
n = input()
steps = raw_input()
N_r = steps.count('R')
N_l = steps.count('L')
d = -1
e = 0
if N_r > N_l:
    s = steps.index('R')+1
    if N_l !=0: e = steps.index('L')
    count = N_r
    d = 1
    
else:
    s = n - steps[::-1].index('L')
    if N_r !=0:e = n - steps[::-1].index('R')+1
    count = N_l
    d=0
    
if e == 0 and d==1:
    e = s+count
elif e==0 and d==0:
    e = s-count


print s,e 
