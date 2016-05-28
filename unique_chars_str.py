#!/usr/bin/env python


#Input = raw_input()
#str_pos = [0]*256
#for i in Input:
#    if str_pos[ord(i)] > 0:
#        print 'NOT unique'
#        exit()
#    else:
#        str_pos[ord(i)]+=1
#
#print "UNIQUE"

#using bit-wise operator

Input = raw_input()
checker = 0
for c in Input:
    val = (ord(c) - ord('a'))
    if checker & ( 1 << val ):
        print 'NOT UNIQUE'
        exit()
    else:
        checker = checker | (1 << val)
print "UNIQUE"