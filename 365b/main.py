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

if a <= 2:
    print(a)
else:
    ans = 2
    tmp = 2
    for i in range(2, a):
        if L[i] == L[i - 1] + L[i - 2]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 2
    ans = max(ans, tmp)
    print(ans)