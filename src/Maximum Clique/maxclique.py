import sys
v, _ = map(int, input().split())
g = [set() for _ in range(v)]
for l in sys.stdin:
    a, b = map(int, l.split())
    g[a].add(b), g[b].add(a)
# Bron–Kerbosch algorithm
def bk(r, p, x):
    if not p and not x: return len(r)
    ans = 0
    for i in p: u = i; break
    for i in x: u = i; break
    for w in [*p]:
        if w in g[u]: continue
        r.add(w); ans = max(ans, bk(r, p&g[w], x&g[w])); r.discard(w), p.discard(w), x.add(w)
    return ans
print(bk(set(), {*range(v)}, set()))