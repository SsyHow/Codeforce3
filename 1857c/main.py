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
t = II()
for _ in range(t):
    b = II()
    L = LII()
    L.sort()
    ans = []
    x = b - 1
    i = 0
    while i < b * (b - 1) // 2:
        ans.append(L[i])
        i += x
        x -= 1
    ans.append(ans[-1])
    print(*ans)