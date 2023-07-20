import sys; input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m): u, v = map(int, input().split()); g[u-1].append(v-1), g[v-1].append(u-1)
a = set(range(n)); b = set()
for _ in range(6):
    for i in range(n):
        if i in a and sum(j in a for j in g[i]) > 1: a.discard(i), b.add(i)
        elif i in b and sum(j in b for j in g[i]) > 1: b.discard(i), a.add(i)
print(2 if b else 1), print(*(i+1 for i in a))
if b: print(*(i+1 for i in b))