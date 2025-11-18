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
L = LII()
x = 0
ans = 1 << 60
for i in range(1, 101):
    tmp = 0
    for j in L:
        if abs(j - i) > 1:
            tmp += abs(j - i) - 1

    if tmp < ans:
        ans = tmp
        x = i
print(x, ans)