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
n, q = MII()
L = LII()
d = {}
x = 0
for i in range(n):
    d[i + 1] = L[i]

s = sum(L)
for i in range(q):
    w = LII()
    if w[0] == 1:
        s += w[2] - d.get(w[1], x)
        d[w[1]] = w[2]
    else:
        s = w[1] * n
        d.clear()
        x = w[1]
    print(s)
