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
from math import gcd, lcm
def range_sum(l, r):
    if l > r:
        return 0
    return (l + r) * (r - l + 1) // 2

for _ in range(II()):
    n, x, y = MII()
    l = lcm(x, y)
    plus = n //x - n // l
    minus = n // y - n // l
    print(range_sum(n - plus + 1, n) - range_sum(1, minus))