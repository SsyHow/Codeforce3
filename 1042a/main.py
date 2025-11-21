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
n = II()
m = II()
L = []
for i in range(n):
    L.append(II())

x = max(L)
high = x + m

miss = 0
for i in L:
    miss += x - i

k = m - miss
if k > 0:
    x += k // n if k % n == 0 else k // n + 1
print(x, high)