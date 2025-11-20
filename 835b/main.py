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
k = II()
n = I()

d = []
for i in n:
    d.append(ord(i) - ord('0'))

d.sort()

cur = sum(d)
ans = 0
for x in d:
    if cur < k:
        cur += 9 - x
        ans += 1
print(ans)