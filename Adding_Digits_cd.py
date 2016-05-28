#!/usr/bin/env python
#http://codeforces.com/problemset/problem/260/A
nums = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
a,b,n = map(int, raw_input().split())
prev = -1
for i in xrange(n):
    for num2 in nums[prev+1:]:
        temp = int(str(a)+str(num2))
        if temp%b==0 and num2!=prev:
            a =temp
            prev=num2
            break
print -1 if len(str(a))<n+1 else a
