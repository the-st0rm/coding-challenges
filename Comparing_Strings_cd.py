#!/usr/bin/env python
#http://codeforces.com/problemset/problem/186/A
s1 = list(raw_input())
s2 = list(raw_input())
L1 = len(s1)
L2 = len(s2)

if L1!=L2:
    print "NO"
    exit()
i=0
sw = 0
while i < L1:
    if s1[i]==s2[i]:
        i+=1
        continue
    elif sw==1:
        sw+=1
        break
    else:
        j = i+1
        f = False
        while j < L1 and not f:
            if s1[j]!=s2[j] and s2[j]==s1[i]:
                temp = s2[i]
                s2[i]=s2[j]
                s2[j]=temp
                f = True
                sw = 1
            j+=1
        if sw==0:
            break
        i+=1
        
if sw==1:
    print "YES"
else:
    print "NO"
