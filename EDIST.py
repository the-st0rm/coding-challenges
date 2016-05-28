#!/usr/bin/env python
#http://www.spoj.com/problems/EDIST/
dp = list()
def sol(i, j, A, B):
    global dp
    if i>=len(A) and j >= len(B):
        return 0
    if i >= len(A):        
        return 10000000
    if j >= len(B):
        return 10000000
    if A[i:] == B[j:]:
        return 0
    if A[i]==B[j]:
        return sol(i+1, j+1, A, B)
    if dp[i][j] != -1:
        return dp[i][j]
    t1 = sol(i+1, j, A, B)+1
    t2 = sol(i, j+1, A, B)+1
    t3 = sol(i+1, j+1, A, B)+1
    dp[i][j]= min(t1,t2,t3)
    return dp[i][j]

T = input()
while T:
    
    A = raw_input();B= raw_input()
    dp = [-1]*len(A)
    for i in range(len(A)):
        dp[i] = [-1]*len(B)
        
    print sol(0, 0, A, B)

    T-=1
    
