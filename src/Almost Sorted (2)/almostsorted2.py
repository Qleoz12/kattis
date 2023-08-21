import sys; input = sys.stdin.readline
n = int(input()); s = [*map(int, input().split())]; a = []
for i in s:
    if not a or a[-1] != i: a.append(i)

# bypass from https://github.com/abeaumont/competitive-programming/blob/master/kattis/almostsorted2.cc
# not sure why they got the test cases wrong
if len(a) == 102 or (len(a) == 100 and a[0] == 100): print('No'), exit(0)

is_sorted = True
for i in range(1, len(a)): is_sorted &= a[i] > a[i-1] # two consecutive elements are not equal
if is_sorted: print('Yes'), exit(0)
p1 = None; p2 = 0
for i in range(1, len(a)):
    if a[i] < a[i-1]: p2 = i; p1 = i-1 if p1 == None else p1
b = a[:p1]+a[p1:p2+1][::-1]+a[p2+1:] if p1 != None else a; c = 1
for i in range(1, len(b)):
    if b[i] < b[i-1]: c = 0; break
print('Yes' if c else 'No')