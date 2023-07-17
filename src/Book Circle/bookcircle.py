import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

B, G = map(int, input().split())
V = B+G

g = [[] for _ in range(V)]
books = []
for _ in range(B+G):
    _, _, *b = input().strip().split()
    books.append({*b})
for i in range(B):
    for j in range(G):
        if books[i]&books[j+B]: g[i].append(j+B)

match, mcbm = [-1]*V, 0
free = set(range(B))
nfree = len(free)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0]*nfree
    mcbm += aug(f)
print(mcbm)