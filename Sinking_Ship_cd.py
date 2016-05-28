#!/usr/bin/env python
#http://codeforces.com/problemset/problem/63/A
import Queue
q = Queue.PriorityQueue()
n = input()
evac = list()
ranks = {"captain":3, "man":2, "woman":1, "child":1, "rat":0}
evac = [0]*4
for i in range(4):
    evac[i]=[]
    
for i in range(n):
    name, rank = raw_input().split(' ')
    r = ranks[rank]
    q.put(r)
    evac[r].append(name)


while not q.empty():
    print evac[q.get()].pop(0)
    
