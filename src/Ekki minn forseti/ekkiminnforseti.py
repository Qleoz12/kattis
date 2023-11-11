import sys; input = sys.stdin.readline
from time import time
n, m = map(int, input().split()); l = [True]*(m+1)
v = [input().strip() for _ in range(m)]
p = [[*map(int, input().split())][::-1] for _ in range(n)]
c = {i:0 for i in {*(q[-1] for q in p)}}
for k in c: l[k] = False
for _ in range(len(c)-1):
    for k in c: c[k] = 0
    for q in p:
        while l[q[-1]]: q.pop()
        c[q[-1]] += 1
    x = min(c.items(), key=lambda x: 2*m*x[1]-x[0])[0]
    l[x] = True; del c[x]
for i in range(1, m+1):
    if l[i] == 0: print(v[i-1]), exit(0)