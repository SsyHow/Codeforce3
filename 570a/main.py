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
dic = {}
for _ in range(m):
    L = LII()
    cand = 1
    x = 0
    for idx, i in enumerate(L):
        if i > x:
            cand = idx + 1
            x = i

    dic[cand] = dic.get(cand, 0) + 1

k = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(k[0][0])
