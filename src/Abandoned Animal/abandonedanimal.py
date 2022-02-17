from heapq import *
import sys

n, k = int(input()), int(input())
minheap, maxheap = {}, {}

for _ in range(k):
    s, i = input().split()
    if i not in minheap:
        minheap[i] = [int(s)]
        maxheap[i] = [-int(s)]
    else:
        minheap[i].append(int(s))
        maxheap[i].append(-int(s))

for i in minheap:
    heapify(minheap[i])
    heapify(maxheap[i])

lo, hi = -1, -n
m = int(input())
minpath, maxpath, items = [], [], []
for _ in range(m):
    items.append(input())

for item in items:
    while minheap[item] and minheap[item][0] < lo:
        heappop(minheap[item])
    try:
        lo = heappop(minheap[item])
        minpath.append(lo)
    except:
        print('impossible')
        sys.exit(0)

for item in items[::-1]:
    while maxheap[item] and maxheap[item][0] < hi:
        heappop(maxheap[item])
    try:
        hi = heappop(maxheap[item])
        maxpath.append(-hi)
    except:
        print('impossible')
        sys.exit(0)

print(['ambiguous', 'unique'][int(minpath == maxpath[::-1])])