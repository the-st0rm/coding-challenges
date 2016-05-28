#!/usr/bin/env python
#http://codeforces.com/problemset/problem/122/A

s1 = set([4,7])
combinations = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
Len = len(combinations)
def test_lucky(num):
    s = set()
    global s1
    for n in num:
        s.add(int(n))
    return (s-s1) == set()


num = input()
if test_lucky(str(num)):
    print 'YES'
else:
    flag =False
    i =0
    while i < Len and not flag:
        if num%combinations[i]==0:
            flag=True
        i+=1
    if flag:
        print 'YES'
    else:
        print 'NO'
            

#print test_lucky('44441777')
