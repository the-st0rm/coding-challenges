#!/usr/bin/env python
#http://codeforces.com/problemset/problem/109/A
n = input()
sevens = n/7
while sevens >=0:
    if (n-(sevens*7))%4==0:
        fours = (n-sevens*7)/4
        print '4'*fours+'7'*sevens
        exit()
    sevens -=1
print -1
