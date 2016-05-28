#!/usr/bin/env python
#http://codeforces.com/problemset/problem/94/A
pass_phrase = raw_input()
counter = 0
d = {}
pf = list()
while counter < len(pass_phrase):
    pf.append(pass_phrase[counter:counter+10])
    counter +=10

password = list()
for i in range(10):
    d[raw_input()]=(i)

for p in pf:
    if p in d:    
        password.append(d[p])
    else:
        print "error: "+str(p)
print ''.join(map(str, password))
