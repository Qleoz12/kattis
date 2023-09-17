n, k = map(int, input().split()); s = []; a = [-1]*n; m = 1
for p in range(n-1, 0, -1):
    if p <= k: k -= p; s.append(p)
    if k == 0: break
for i in s[::-1]: a[i-1] = n; n -= 1
for i in range(len(a)):
    if a[i] == -1: a[i] = m; m += 1
print(*a)