#!/usr/bin/env python
#http://codeforces.com/problemset/problem/332/B

n, k = map(int, raw_input().split())

arr = map(int , raw_input().split())
sums = list()
prev = 0
for val in arr[:k]:
    prev+=val
i =k
sums.append((prev, 0))
while i < n:
    s = prev - arr[i-k]+arr[i]
    sums.append((s, i-k+1))
    prev = s
    i+=1
sums.sort(key=lambda x: (x[0], -1 * x[1]), reverse=True)
s1 =  sums[0]
output=[s1]
for s in sums[1:]:
    if abs(s[1] - s1[1])>=k:
        output.append(s)
        break
output.sort(key=lambda x: (x[1]))
print output[0][1]+1, output[1][1]+1 
