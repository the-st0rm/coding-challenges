#!/usr/bin/env python
#http://codeforces.com/problemset/problem/131/A
word = raw_input()
if word[1:].isupper():
    new_word = list()
    for l in word:
        if l.islower():
            new_word.append(l.upper())
        elif l.isupper():
            new_word.append(l.lower())
        else:
            new_word.append(l)
            
    print ''.join(new_word)
else:
    print "%s" %(word)
