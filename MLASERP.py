#!/usr/bin/env python
#http://www.spoj.com/problems/MLASERP/
import Queue
#f = open('input', 'r')
Input = map(int, raw_input().split(' '))
w = Input[0]
h = Input[1]


visited= [0]*h
graph = [0]*h
mirrors = [0]*h
for i in range(h):
    graph[i] = [-1]*w
    visited[i] = [0]*w
    mirrors[i] = [-1]*w
    
start=[]
for row in range(h):
    line = raw_input()
    for col in range(w):
        if line[col] =='.': graph[row][col]=1
        elif line[col]=='*': graph[row][col]=-1
        elif line[col]=='C':graph[row][col]=0;start.append([row, col])



q = Queue.Queue()                    
q.put((0, (start[0]), 'S'))


flag = True
while not q.empty() and flag:
    node = q.get()
    y=node[1][0];x=node[1][1]    
    if visited[y][x] == 0 and graph[y][x]!=-1:
        visited[y][x]=1
        mirrors[y][x] = node[0]
        if y+1 < h and graph[y+1][x]!=-1:
            if node[2]=='V' or node[2]=='S':
                q.put((mirrors[y][x], [y+1, x], 'V'))
            else:
                q.put((1+mirrors[y][x], [y+1, x], 'V'))
        if y-1 >=0 and graph[y-1][x] != -1:
            if node[2]=='V' or node[2]=='S':
                q.put((mirrors[y][x], [y-1, x], 'V'))
            else:
                q.put((1+mirrors[y][x], [y-1, x], 'V'))          
        if x+1 < w and graph[y][x+1] != -1:
            if node[2]=='H' or node[2]=='S':
                q.put((mirrors[y][x], [y, x+1], 'H'))
            else:
                q.put((1+mirrors[y][x], [y, x+1], 'H'))
        if x-1 < w and graph[y][x-1] != -1:
            if node[2]=='H' or node[2]=='S':
                q.put((mirrors[y][x], [y, x-1], 'H'))
            else:
                q.put((1+mirrors[y][x], [y, x-1], 'H'))
        
        if start[1][0]==y and start[1][1]==x:
            flag = False
print mirrors[start[1][0]][start[1][1]]

