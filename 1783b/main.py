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
    n = II()
    l = 1
    r = n * n

    k = 0
    L = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if k:
                L[i][j] = l
                l += 1
            else:
                L[i][j] = r
                r -= 1

            k ^= 1
        if (i & 1):
            L[i] = L[i][::-1]
    for i in L:
        print(*i)