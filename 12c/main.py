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
n, m = MII()
L = LII()
L.sort()
dic = {}
for i in range(m):
    s = I()
    dic[s] = dic.get(s, 0) + 1
k = len(dic)
M = sorted(dic.values(), reverse=True)

minx = sum(M[i] * L[i] for i in range(k))
maxx = sum(M[i] * L[n - i - 1] for i in range(k))
print(minx, maxx)
