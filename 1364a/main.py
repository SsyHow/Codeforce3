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
for _ in range(a):
    n, x = MII()
    L = LII()

    l = -1
    k = 0
    for i in range(n):
        if L[i] % x:
            if l == -1:
                l = i
            r = i
        k += L[i]

    if k % x:
        print(n)
    elif l == -1:
        print(-1)
    else:
        print(n - min(l + 1, n - r))