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
    a, b, c, d = MII()
    x, y, x1, y1, x2, y2 = MII()
    if (x2 - x1 == 0 and a * b > 0) or (y2 - y1 == 0  and c * d > 0):
        print("No")
    elif x1 <= x - a + b <= x2 and y1 <= y - c + d <= y2:
        print("Yes")
    else:
        print("No")