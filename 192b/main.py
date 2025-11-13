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

M = sorted(L)

def check(s):
    if s[0] <= 0 or s[-1] <= 0:
        return True
    for i in range(a - 1):
        if s[i] == s[i + 1] == 0:
            return True
    return False

ans = 0
i = 0
while i < a:
    ans = M[i]
    for j in range(a):
        if L[j] == ans:
            L[j] = 0

    if check(L):
        break
    i += 1
print(ans)