#!/usr/bin/env python
#http://codeforces.com/problemset/problem/29/C
n = input()
s = 100
e = 1
g = dict()
visited = set()
m =100000000
m2=100000000
for i in xrange(n):
    n1, n2 = map(int, raw_input().split())
    #if i==0: s=n1
    #if i==n-1:e=n2
    if n1 in g:
        g[n1].add(n2)
    else:
        g[n1]=set()
        g[n1].add(n2)

    if n2 in g:
        g[n2].add(n1)
    else:
        g[n2]=set()
        g[n2].add(n1)
    
    if len(g[n1]) < m:
            m = len(g[n1])
            s = n1
    if len(g[n2]) < m:
            m= len(g[n2])
            s = n2

        
path = list()
st = list()
st.append((s, [s]))
pathes = dict()
pathes[s]=[s]
found = False
sol = [s]
while len(st)>0 and not found:
    (node, p) = st.pop()
    if node not in visited:
        visited.add(node)
        path.append(node)
        for nn in g[node]:
            if nn not in visited:
                st.append((nn, p+[node]))
                pathes[nn]= p+[node]
                if len(pathes[nn]+[nn])> len(sol):
                    sol = pathes[nn]+[nn]
                #if nn in pathes: pathes[nn]= p+[nn]
                #else: pathes[nn]=p+[nn]
                #pathes.append((nn, path+[nn]))
            
printed = set()
final_res = list()
for i in sol:
    if i not in printed:
        final_res.append(i)
        printed.add(i)
print ' '.join(map(str, final_res))
