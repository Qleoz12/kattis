def C(n, r):
    r = min(r, n-r)
    if n < r: return 0
    if r == 0 or r == n: return 1
    if r == 1 or r == n-1: return n
    f = 1
    for i in range(r): f *= n-i; f //= i+1
    return f

n = int(input())
dp = [1]*(n+1)
for k in range(3, n+1): dp[k]= (k-1)**k-sum(dp[i]*C(k-1,i-1)*(k-i-1)**(k-i) for i in range(2,k-1))
print(dp[n]/((n-1)**n))