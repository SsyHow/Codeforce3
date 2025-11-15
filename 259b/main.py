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
L = []
for i in range(3):
    L.append(LII())

k = (L[0][2] + L[2][0]) // 2
L[0][0] = k - (L[0][1] - L[1][2]) // 2
L[2][2] = k * 2 - L[0][0]
L[1][1] = L[0][0] + L[0][1] + L[0][2] - k * 2
for i in L:
    print(*i)

