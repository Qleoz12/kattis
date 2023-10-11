import sys; input = sys.stdin.readline
for T in range(int(input())):
    N, *V = map(int, input().split())
    S = sum(V); X = 2*S/N; L = 200 # X = (S+S')/N'
    while X < L:
        A = [i for i in V if i <= X]
        X, L = (S+sum(A))/len(A), X
    print(f'Case #{T+1}:', *(max((X-i)/S*100, 0) for i in V))