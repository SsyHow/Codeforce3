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
    s = I()
    s += s
    k = z = 0
    for c in s:
        z = z + 1 if c == '1' else 0
        k = max(k, z)

    n = len(s) // 2
    if k > n:
        print(n*n)
    else:
        sa = (k + 1) // 2
        sb = (k + 2) // 2
        print(sa * sb)