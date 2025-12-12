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

def s(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans
res = [0] * (2* 10 ** 5 + 1)
res[0] = 1
i = 0
for i in range(1, 2 * 10 ** 5 + 1):
    res[i] = res[i - 1] + s(i + 1)

a = II()
for _ in range(a):
    b = II()
    print(res[b - 1])
