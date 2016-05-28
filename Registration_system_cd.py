#!/usr/bin/env python
#http://codeforces.com/problemset/problem/4/C
d = dict()
n = input()
for i in range(n):
    name = raw_input()
    if name in d:
        d[name]+=1
        print name+str(d[name])
    else:
        print 'OK'
        d[name]=0
        
