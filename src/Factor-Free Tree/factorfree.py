n, a = int(input()), list(map(int, input().split()))
pr = [None]*n

LIMIT = max(a)
spf = list(range(LIMIT + 1))

p = 2
while p <= LIMIT:
    if spf[p] == p:
        for i in range(2*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

def pf(n):
    res = []
    while n != 1:
        res.append(spf[n])
        n //= spf[n]
    return res

pfs, pft = list(map(pf, a)), {}
pred, succ = [-1]*(n+1), [n]*(n+1)
for i, e in enumerate(pfs):
    for f in e:
        if f not in pft: pft[f] = []
        if pft[f]:
            b = pft[f][-1]
            if b == i: continue
            pred[i], succ[b] = max(pred[i], b), min(succ[b], i)
        pft[f].append(i)

def solve(l, r):
    stack = [(l, r, 0)]
    while stack:
        l, r, prev = stack.pop()
        for t in range(r-l):
            if t % 2: i = r - (t+1)//2
            else: i = l + t//2
            if succ[i] >= r and (i == -1 or pred[i] < l):
                pr[i] = prev
                if l < i: stack.append((l, i, i+1))
                if i+1 < r: stack.append((i+1, r, i+1))
                break

solve(0, n)
if None in pr: print('impossible')
else: print(*pr)