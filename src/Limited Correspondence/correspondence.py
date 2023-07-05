from sys import stdin
input = stdin.readline

def solve(t):
    n = int(input())
    a, b = [], []
    for _ in range(n):
        aa, bb = input().strip().split()
        a.append(aa), b.append(bb)
    best = ['|'*1105]
    def backtrack(sa='', sb='', u=[0]*n):
        if max(len(sa), len(sb)) > len(best[0]): return
        if sa and sa == sb and (len(sa) < len(best[0]) or (len(sa) == len(best[0]) and sa < best[0])): best[0] = sa; return
        for i in range(n):
            if u[i]: continue
            ta, tb, ok = sa+a[i], sb+b[i], 1
            for j in range(min(len(sa), len(sb)), min(len(ta), len(tb))):
                if ta[j] != tb[j]: ok = 0; break
            if ok: u[i] = 1; backtrack(ta, tb, u); u[i] = 0
    backtrack()
    print(f'Case {t}: {best[0] if len(best[0]) != 1105 else "IMPOSSIBLE"}')
    return t+1

t = 1
while True:
    try: t = solve(t)
    except: break