def f(x):
    it = 0
    while x != 1:
        if x % 2: x += 1
        else: x //= 2
        it += 1
    return it

def g(x):
    if x < 2: return 0
    if x%2: return (g(x-1) + f(x)) % MOD
    return (2*g(x//2) + 3*x//2 - 2) % MOD

MOD = 10**9 + 7
l, r = map(int, input().split())
print((g(r)-g(l-1)) % MOD)