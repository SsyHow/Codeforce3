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
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n, m, k = MII()
L = LII()
M = LII()
c = LII()
dic = defaultdict(int)

for i in range(n):
    dic[M[i]] = max(dic[M[i]], L[i])

ans = 0
for i in c:
    if dic[M[i - 1]] != L[i - 1]:
        ans += 1
print(ans)

