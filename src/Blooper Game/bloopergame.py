import sys; input = sys.stdin.readline
from heapq import *
N, L, P = map(float, input().split()); A = 1; N, L = round(N), round(L)
Q = [1/int(input()) for _ in range(N)]; heapify(Q)
while L: heappush(Q, heappop(Q)**(P**(c:=(L+N-1)//N))); L -= c
for i in Q: A *= i
print(A)