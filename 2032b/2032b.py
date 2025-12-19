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

for _ in range(II()):
    n, k = MII()
    if n == 1:
        print(1, 1)
    elif k == 1 or k == n:
        print(-1)
    elif k % 2 == 0:
        print(3, 1, k, k + 1)
    else:
        print(5, 1, 2, k, k + 1, k + 2)
