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
from random import getrandbits
RD = getrandbits(31)
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    b = II()
    L = LII()

    dic = defaultdict(int)
    for i in L:
        dic[i] += 1

    ans = 0

    prev = 0
    for x in sorted(dic):
        if dic[x] >= dic[x -1]:
            ans += dic[x] - dic[x -1]
    print(ans)

    # L.sort()
    # dic = Counter(L)
    #
    # ans = 0
    #
    # for x in dic.keys():
    #     if dic[x] >= dic[x - 1]:
    #         ans += dic[x] - dic[x - 1]
    # print(ans)