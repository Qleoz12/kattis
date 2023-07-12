import sys; input = sys.stdin.readline
from math import hypot
INF = 1e18
P = 10**6

N, S, T, Q = map(int, input().split())

def add_edge(u, v, c, w):
    e1, e2 = [u, v, c, w, 0, len(al[v])], [v, u, 0, -w, 0, len(al[u])]
    al[u].append(len(el)), el.append(e1), al[v].append(len(el)), el.append(e2)

n = N+2
al, el, k = [[] for _ in range(n)], [], INF
pos = []
for _ in range(N):
    x, y, h = map(int, input().split())
    pos.append((x, y, h))
for i in range(N-1):
    xi, yi, hi = pos[i]
    for j in range(i+1, N):
        xj, yj, hj = pos[j]
        if (d:=hypot(xi-xj, yi-yj, hi-hj)) <= Q:
            if hi > hj: add_edge(i, j, N, int(P*d))
            elif hi < hj: add_edge(j, i, N, int(P*d))
s, t = N, N+1
for i in map(int, input().split()): add_edge(s, i-1, 1, 0)
for i in map(int, input().split()): add_edge(i-1, t, 1, 0)

flow = cost = 0
while flow < k:
    id, d, q, p, pe, qh, qt = [0]*n, [INF]*n, [0]*n, [0]*n, [0]*n, 0, 0
    q[qt] = s; qt += 1; d[s] = 0
    while qh != qt:
        v = q[qh]; qh += 1
        id[v] = 2
        if qh == n: qh = 0
        for i in range(len(al[v])):
            r = el[al[v][i]]
            if r[4] < r[2] and d[v]+r[3] < d[r[1]]:
                d[r[1]] = d[v]+r[3]
                if id[r[1]] == 0:
                    q[qt] = r[1]; qt += 1
                    if qt == n: qt = 0
                elif id[r[1]] == 2:
                    qh -= 1
                    if qh == -1: qh = n-1
                    q[qh] = r[1]
                id[r[1]] = 1; p[r[1]] = v; pe[r[1]] = i
    if d[t] == INF: break
    addflow, v = k-flow, t
    while v != s:
        ee = al[p[v]][pe[v]]
        addflow = min(addflow, el[ee][2]-el[ee][4])
        v = p[v]
    v = t
    while v != s:
        ee = al[p[v]][pe[v]]
        el[ee][4] += addflow
        el[al[v][el[ee][5]]][4] -= addflow
        cost += el[ee][3]*addflow
        v = p[v]
    flow += addflow
print(cost/P if flow == T else 'IMPOSSIBLE')