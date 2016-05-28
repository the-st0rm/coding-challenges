#!/usr/bin/env python

n,k=map(int, raw_input().split())
a = map(int, raw_input().split())

i=n-1
while i >=0:
    if a[i]!=a[i-1]:
        break
    i-=1
if i < k:
    print i;
else:
    print -1