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
    L1 = LII()
    L2 = LII()
    L3 = LII()

    k1 = k2 = k3 = 0
    for i in L1:
        if k1 | i | x != x:
            break
        k1 |= i
    for i in L2:
        if k2 | i | x != x:
            break
        k2 |= i
    for i in L3:
        if k3 | i | x != x:
            break
        k3 |= i

    print("Yes" if k1 | k2 | k3 == x else "No")

