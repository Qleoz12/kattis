import sys; input = sys.stdin.readline
n, m = map(int, input().split())
a = [*map(int, input().strip())]; r = 0
for i in range(n):
    if a[i]:
        r += 1; a[i] = 0
        if i+2 < n: a[i+2] += a[i+1]; a[i+1] = 0
print(r)