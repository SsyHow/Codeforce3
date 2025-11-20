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

L = []
f = True
for _ in range(a):
    if f:
        s = 'WB' * (a // 2) + 'W' * (a % 2)
        L.append(s)
    else:
        s = 'BW' * (a // 2) + 'B' * (a % 2)
        L.append(s)
    f = not f
for i in L:
    print(''.join(i))