#!/usr/bin/env python
#http://codeforces.com/problemset/problem/222/A
n,k=map(int, raw_input().split())
a = map(int, raw_input().split())


if len(a)==1:
    print 0
    exit()
i=n-1
flag = True
while i>k-1:
    if a[i]==a[i-1]:
        i-=1
    else:
        flag = False
        break
ll = len(a[:k-1])
if flag:
    c = -1
    for i in range(ll):
        if a[i]!=a[k-1]:
            c = i
    print c+1
else:
    print -1
