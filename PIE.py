#!/usr/bin/env python
#http://www.spoj.com/problems/PIE/
import math

PIES = [];N=0;F=0
def calc_vol(r):
    return math.pi * (r**2)

def test_val(PIES, val):    
    counter =0
    no_f = 0
    copy_pies = list(PIES)
    while counter<len(copy_pies) and no_f != F:
        if copy_pies[counter]-val >=0:
            no_f+=1
            copy_pies[counter]=copy_pies[counter]-val
        else:
            counter +=1
    return no_f==F
def bin_search():
    global PIES, N,F
    end = max(PIES)
    start =0
    while start<end:
        mid = (start+end)/2.0
        if test_val(PIES, mid):
            start = mid+0.0000001
        else:
            end = mid
    return start -0.0000001

T = input()
while T>0:
    
    Input = map(int, raw_input().split(' '))
    N,F = Input[0], Input[1]
    F+=1
    PIES = []
    if N==1:
        r = input()
        PIES.append(calc_vol(r))
    else:
        row = map(int, raw_input().split(' '))
        for i in row:
            PIES.append(calc_vol(i))
    
    print round(bin_search(),4)   
    
    T-=1
