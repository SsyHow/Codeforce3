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
n = II()
L = LII()
m = II()
k = sum(L)
ans = 1 << 60
for _ in range(m):
    l, r = MII()
    if k > r:
        continue
    ans = min(ans, max(k, l))
print(ans if ans != 1 << 60 else -1)
