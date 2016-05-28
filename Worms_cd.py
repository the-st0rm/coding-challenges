#!/usr/bin/env python

n = input()
piles  = map(int, raw_input().split(' '))
all_worms = list()
for i in range(len(piles)):
    all_worms += [i+1]*piles[i]
#print all_worms
#exit()
m = input()
jucy = map(int, raw_input().split(' '))
output = list()
for j in jucy:
    output.append(all_worms[j-1])
for val in output:
    print val