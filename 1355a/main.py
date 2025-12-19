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

def getAdd(n):
    m1 = 10
    m2 = 0
    while n:
        m1 = min(n%10, m1)
        m2 = max(m2, n%10)
        n //= 10
    return m1 * m2
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    n, k = MII()
    k -= 1
    while k:
        y = getAdd(n)
        if y == 0:
            break
        n += y
        k -= 1
    print(n)