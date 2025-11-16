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
a, b = MII()

while (a >= 2 * b or b >= a * 2) and a != 0 and b != 0:
    if a >= 2 * b:
        a = a % (b * 2)
    elif b >= a * 2:
        b = b % (a * 2)
    else:
        break
print(a, b)

