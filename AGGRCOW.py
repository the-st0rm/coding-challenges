#!/usr/bin/env python
#http://www.spoj.com/problems/AGGRCOW/

T = input()
stalls = list()
N=0;C=0;Min=1;Max=-1

def test_bin(max_len):
    j=0
    i=1
    global stalls,N,C
    n_cows = 1
    if n_cows==C:
        return True
    while i <N and n_cows<C:
        if stalls[i]-stalls[j]<max_len:
            i+=1
        else:
            j=i
            n_cows+=1
            i+=1
    return (n_cows==C)
    

def BinSearch():
    start = 0;end=stalls[N-1]
    while(start < end)
    {
        Mid = (start+end)/2
        if test_bin(Mid):
            start = Mid+1
        else:
            end=Mid
    }
    return start-1


while T>0:
    stalls = list()
    Input = map(int, raw_input().split(' '))
    N,C = Input[0], Input[1]
    
    for i in range(N):
        stalls.append(input())
    stalls.sort()
    print BinSearch()
    T -=1
    
