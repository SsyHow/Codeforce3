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
    b = II()
    L = LII()

    dp = [[0 for _ in range(b + 1)] for _ in range(2)]

    for i in range(1, b + 1):
        dp[i & 1][L[i - 1]] = max(dp[i & 1][L[i - 1]], dp[(i ^ 1) & 1][L[i - 1]] + 1)

    for i in range(1, b + 1):
        print(max(dp[0][i], dp[1][i]), end = ' ')
    print()