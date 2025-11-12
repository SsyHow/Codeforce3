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


def calc(s):
    ans = 0
    while s:
        ans += s % 10
        s //= 10
    return ans
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
k = 9
t = 0
while k < a:
    k *= 10
    k += 9
    t *= 10
    t += 9

print(calc(a - t) + calc(t))