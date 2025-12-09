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
def f(x):
    ans = 0
    n = len(x)
    x = x[::-1]
    for i in range(n):
        ans += n **  (n - i + 1) * x[i]
    return ans
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    n = II()
    a = LII()



    ind, ce, ans = [0] * n, n, []
    for i in range(n): ind[n - a[i]] = i
    for i in ind:
        if i < ce:
            ans += a[i:ce]
            ce = i
    print(*ans)