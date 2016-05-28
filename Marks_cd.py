#!/usr/bin/env python
#http://codeforces.com/problemset/problem/152/A
import re

n,m = map(int, raw_input().split())
graph = [0]*m
for i in range(m):
    graph[i]=[]
for i in range(n):
    g = raw_input()
    for j in range(m):
        graph[j].append(g[j])
    
s = set()
for i in range(m):
    students = [m.start() for m in re.finditer(str(max(graph[i])), str(graph[i]))]
    for j in students:
        s.add(j)

print len(s)
