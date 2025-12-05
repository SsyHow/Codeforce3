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
    r, c = MII()

    left = []
    right = []

    for i in range(r):
        L = list(I())
        if i == 0:
            t = L.copy()
        if i == r - 1:
            b = L.copy()

        left.append(L[0])
        right.append(L[-1])

    if 'W' in t and 'W' in b and 'W' in left and 'W' in right:
        print("YES")
    elif 'B' in t and 'B' in b and 'B' in left and 'B' in right:
        print("YES")
    else:
        print("NO")
