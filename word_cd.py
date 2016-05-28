#!/usr/bin/env python
#http://codeforces.com/problemset/problem/474/B

word = raw_input()

lower=0;upper=0
for l in word:
    if l.isupper():
        upper+=1
    else:
        lower+=1
        
if lower>=upper:
    print word.lower()
else:
    print word.upper()
