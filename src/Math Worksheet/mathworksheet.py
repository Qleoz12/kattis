fi = True
while True:
    n = int(input())
    if n == 0: break
    elif fi: fi = False
    else: print()
    res = []
    tl = []
    for _ in range(n):
        res.append(str(eval(input())))
        tl.append(len(res[-1]))
    width = max(tl)
    cols = 51 // (width + 1)
    for i in range(n):
        if i % cols == cols-1 or i == n-1:
            print(' '*(width-tl[i])+res[i])
        else:
            print(' '*(width-tl[i])+res[i], end=' ')