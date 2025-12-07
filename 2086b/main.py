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
for _ in range(a):
    n, k, x = MII()
    L = LII()

    if sum(L) * k < x:
        print(0)
        continue

    l = 1
    r = n * k

    while l <= r:
        m = l + (r - l) // 2
        cnta = (n * k - m + 1) // n
        suff = (n * k - m + 1) % n
        summ = cnta * sum(L)

        for i in range(n - suff, n):
            summ += L[i]

        if summ < x:
            r = m - 1
        else:
            l = m + 1

    print(r)