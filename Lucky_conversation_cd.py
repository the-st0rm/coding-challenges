#!/usr/bin/env python
#http://codeforces.com/problemset/problem/145/A
def ops(s1, s2):
    if s1==s2:
        return 0
    if len(s1)==2:
        if s1[0]==s2[0] or s1[1]==s2[1]:
            return 1
        elif s1[1]==s2[0] and s1[0]==s2[1]:
            return 1
        else:
            return 2
    else:
        return 1
        
s1 = raw_input()
s2 = raw_input()

L  = len(s1)
sol = 0
counter = 0
while counter <= (L-1):
    sol+=ops(s1[counter:counter+2], s2[counter:counter+2])
    counter +=2
print sol
