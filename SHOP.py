#!/usr/bin/env python
#http://www.spoj.com/problems/SHOP/
import Queue
run = True
while run:
    Input = map(int, raw_input().split(' '))
    w, h = Input[0], Input[1]
    if w == 0 and h == 0:
        run = False
        continue
    graph = [0]*h
    visited = [0]*h
    dist = [0]*h
    for i in range(h):
        graph[i] = [-1]*w
        visited[i] = [0]*w
        dist[i] = [0]*w
    for i in range(h):
        row = raw_input()
        for j in range(len(row)):
            if row[j] =='X': continue
            elif row[j] == 'S': graph[i][j]=0;start=(i,j)
            elif row[j] == 'D': graph[i][j]=0;end=(i,j)
            else: graph[i][j]=int(row[j])
    q = Queue.PriorityQueue()
    q.put((0, start))
    flag = True
    while not q.empty() and flag:
        node = q.get()
        y = node[1][0]
        x = node[1][1]
        if visited[y][x] == 0:
            visited[y][x] = 1
            dist[y][x]=node[0]
            if y+1 < h and graph[y+1][x]!= -1 and visited[y+1][x] == 0:q.put((node[0]+graph[y+1][x], (y+1, x)))
            if y-1 >= 0 and graph[y-1][x]!= -1 and visited[y-1][x] == 0:q.put((node[0]+graph[y-1][x], (y-1, x))) 
            if x+1 < w and graph[y][x+1]!= -1 and visited[y][x+1] == 0:q.put((node[0]+graph[y][x+1], (y, x+1)))    
            if x-1 >=0 and graph[y][x-1]!= -1 and visited[y][x-1] == 0:q.put((node[0]+graph[y][x-1], (y, x-1)))
    print dist[end[0]][end[1]]
    raw_input()







#why it is not working !!! ?? 
##!/usr/bin/env python
#import Queue
#run = True
#while run:
#    
#    Input = map(int, raw_input().split(' '))
#    w, h = Input[0], Input[1]
#    if w == 0 and h == 0:
#        run = False
#        continue
#    
#    graph = [0]*h
#    visited = [0]*h
#    dist = [0]*h
#    for i in range(h):
#        graph[i] = [-1]*w
#        visited[i] = [0]*w
#        dist[i] = [0]*w
#    
#    
#    
#    
#    for i in range(h):
#        row = raw_input()
#        for j in range(len(row)):
#            if row[j] =='X': continue
#            elif row[j] == 'S': graph[i][j]=0;start=(i,j)
#            elif row[j] == 'D': graph[i][j]=0;end=(i,j)
#            else: graph[i][j]=int(row[j])
#    
#        
#    
#    res = 0
#    q = Queue.PriorityQueue()
#    q.put((0, start))
#    
#    flag = True
#    while not q.empty() and flag:
#        node = q.get()
#        y = node[1][0]
#        x = node[1][1]
#        if visited[y][x] == 0:
#            visited[y][x] = 1
#            dist[y][x]=node[0]
#            #process the node
#            
#            
#            if y+1 < h and graph[y+1][x]!= -1 and visited[y+1][x] == 0:
#                q.put((node[0]+graph[y+1][x], (y+1, x)))
#                if graph[y+1][x]==0:
#                    flag = False
#                    res = node[0]+graph[y+1][x]
#                    
#            if y-1 >= 0 and graph[y-1][x]!= -1 and visited[y-1][x] == 0:
#                q.put((node[0]+graph[y-1][x], (y-1, x)))
#                #if graph[y-1][x]==0:
#                #    flag = False
#                #    res = node[0]+graph[y-1][x]
#                    
#            if x+1 < w and graph[y][x+1]!= -1 and visited[y][x+1] == 0:
#                q.put((node[0]+graph[y][x+1], (y, x+1)))
#                if graph[y][x+1]==0:
#                    flag = False
#                    res = node[0]+graph[y][x+1]
#                    
#            if x-1 >=0 and graph[y][x-1]!= -1 and visited[y][x-1] == 0:
#                q.put((node[0]+graph[y][x-1], (y, x-1)))
#                if graph[y][x-1]==0:
#                    flag = False
#                    res = node[0]+graph[y][x-1]
#                
#            
#    print res
#    raw_input()
