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
    x, y, z, k = MII()
    ans = 0
    for i in range(1,x + 1):
        for j in range(1, y + 1):
            if (k % (i * j)):
                continue
            c = k // (i * j)
            if c > z:
                continue
            ways = (x - i + 1) * (y - j + 1) * (z - c + 1)
            ans = max(ans, ways)
    print(ans)