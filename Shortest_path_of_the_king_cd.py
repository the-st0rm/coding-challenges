#!/usr/bin/env python
import Queue

LOC = {'1':0, '2':1, '3':2, '4':3,'5':4,'6':5,'7':6,'8':7,'a':0, 'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}


src = raw_input()
src= [LOC[src[0]], LOC[src[1]]]
dst = raw_input()
dst= [LOC[dst[0]], LOC[dst[1]]]


dim = 8
graph = [0]*dim
visited = [0]*dim
for i in range(dim):
    graph[i]=[0]*dim
    visited[i]=[0]*8    
    
    
def bfs_path(graph, src, goal):
    path =[]
    q = [(src, path)]
    while q:
        v, path = q.pop(0)
        x = v[0];y=v[1]
        if visited[x][y]==0:
            visited[x][y]=1
            if y+1 < dim and visited[x][y+1]==0:
                q.append(([x, y+1], path+['U']))
            if y-1 >=0 and visited[x][y-1]==0:
                q.append(([x, y-1], path+['D']))
            if x+1 < dim and visited[x+1][y]==0:
                q.append(([x+1, y], path+['R']))
            if x-1 >=0 and visited[x-1][y]==0:
                q.append(([x-1, y], path+['L']))
            if x+1 < dim and y+1 < dim and visited[x+1][y+1]==0:
                q.append(([x+1, y+1], path+['RU']))
            if x-1 >=0 and y-1 >=0 and visited[x-1][y-1]==0:
                q.append(([x-1, y-1], path+['LD']))
            if x-1 >=0 and y+1 <dim and visited[x-1][y+1]==0:
                q.append(([x-1, y+1], path+['LU']))
            if x+1 <dim and y-1 >=0 and visited[x+1][y-1]==0:
                q.append(([x+1, y-1], path+['RD']))
                
            if [x, y] == goal:
                return path
                

test = list()


path= bfs_path(graph, src, dst)
print len(path)
for p in path:
    print p    