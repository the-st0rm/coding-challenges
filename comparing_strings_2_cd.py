#!/usr/bin/env python

str1 = list(raw_input());str2=list(raw_input())
if len(str1) != len(str2):
    print 'NO'
else:
    str1.sort();str2.sort()
    for i in xrange(len(str1)):
        if str1[i]!=str2[i]:
            print 'NO'
            exit()
    print 'YES'
        
    
