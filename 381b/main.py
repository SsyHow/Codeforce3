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
d = {}
for i in L:
    d[i] = d.get(i, 0) + 1

ans = []
bac = []
k = max(d)
for i in sorted(d):
    ans.append(i)
    if d[i] >= 2:
        bac.append(i)

if bac and bac[-1] == ans[-1]:
    bac.pop()
print(len(ans) + len(bac))
print(*(ans + bac[::-1]))