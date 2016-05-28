#!/usr/bin/env python
#http://www.spoj.com/problems/MICEMAZE/
import Queue



N = input();E = input();T = input();M = input()
visited = [0]*N
dist = [-1]*N
arr = [0]*N

for i in range(N):
    arr[i] = []

for i in range(M):
    path = map(int, raw_input().split(' '))
    arr[path[1]-1].append((path[2], path[0]-1)) #trick bent gazmaaaa I need to reverse the connection
    
q = Queue.PriorityQueue()
q.put((0, E-1))

while (not q.empty()):
    current = q.get()
    if visited[current[1]] == 0:
        visited[current[1]] = 1
        dist[current[1]] = current[0]
        for val in arr[current[1]]:
            q.put((val[0]+current[0], val[1]))
        
        
res =0
for val in dist:
    if val <= T and val != -1:
        res +=1

print res
