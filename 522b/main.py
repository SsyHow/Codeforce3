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
a = II()
s = 0
L = []
fir, sec = 0, 0
for _ in range(a):
    x, y = MII()
    L.append((x, y))
    s += x
    if y > fir:
        sec = fir
        fir = y
    elif y > sec:
        sec = y
ans = []
for x, y in L:
    # print(fir)
    ans.append((s - x) * fir if y < fir else (s - x) * sec)

print(*ans, sep = ' ')