#!/usr/bin/env python
#http://www.spoj.com/problems/BITMAP/
import Queue

h=0;w=0
graph=0
dist=0
vis=0

def bfs(start):
    vis=[0]*h
    for i in range(h):
        vis[i]=[0]*w
        
    q = Queue.Queue()
    q.put((0, start))
    while not q.empty():
        node = q.get()
        y=node[1][0];x=node[1][1]
        if vis[y][x] == 0:
            vis[y][x] =1
            dist[y][x]=node[0]
            if y+1 < h and graph[y+1][x] != 1 and dist[y][x]+1 < dist[y+1][x]:
                q.put((dist[y][x]+1, [y+1,x]))
            if y-1 >= 0 and graph[y-1][x] != 1 and dist[y][x]+1 < dist[y-1][x]:
                q.put((dist[y][x]+1, [y-1,x]))
            if x+1 < w and graph[y][x+1] != 1 and dist[y][x]+1 < dist[y][x+1]:
                q.put((dist[y][x]+1, [y,x+1]))
            if x-1 >= 0 and graph[y][x-1] != 1 and dist[y][x]+1 < dist[y][x-1]:
                q.put((dist[y][x]+1, [y,x-1]))
                
    
    



T = input()
while T > 0:
    
    Dimen = map(int, raw_input().split())
    h=Dimen[0];w=Dimen[1]
    
    dist=[0]*h
    vis=[0]*h
    graph=[-1]*h
    for i in range(h):
        dist[i]=[10000]*w
        vis[i]=[0]*w
        graph[i]=[-1]*w
        
        
    whites = list()
    for i in range(h):
        line = raw_input()
        for j in range(w):
            if line[j] =='0':graph[i][j]=0
            elif line[j]=='1':graph[i][j]=1;whites.append([i,j]);dist[i][j]=0
    
    for pixel in whites:
        bfs(pixel)
    
    for row in dist:
        print str(row).strip('[]').replace(',', '')
    
    T -=1
