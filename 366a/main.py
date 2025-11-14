import sys

input = lambda: sys.stdin.readline().rstrip()


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
k = II()
L = []
for _ in range(4):
    L.append(LII())

xx = (-1, 0, 0)

for i in range(4):
    a, b, c, d = L[i]
    if min(a, b) + min(c, d) <= k:
        xx = (i + 1, min(a, b), k - min(a, b))
if xx[0] > 0:
    print(*xx)
else:
    print(-1)