#!/usr/bin/env python



def sub_sum(arr, start, end):
    counter = start
    S = 0
    while counter < end:
        S +=arr[counter]
        counter +=1
    return S

N = input()
bro_1 = list(); bro_2=list()

arr = map(int, raw_input().split(' '))
arr.sort(reverse=True)
flag = False
counter = 0
Len = len(arr)
start = 0
Sum = sum(arr)
while counter <= Len:
    S1 = sub_sum(arr, start, counter)
    S2 = Sum-S1
    if S1 > S2:
        sol = counter - start
        counter = Len+1
    else:
        counter +=1
print sol