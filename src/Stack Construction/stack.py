import sys
input()
for l in sys.stdin:
    l = l.strip(); n = len(l)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 2
    for j in range(n):
        for i in range(j):
            dp[i][j] = 2+dp[i][j-1]
            for k in range(i, j):
                if l[j] == l[k] and dp[i][j] > (m:=dp[i][k]+dp[k+1][j-1]): dp[i][j] = m
    print(n+dp[0][-1])