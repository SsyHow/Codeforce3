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
t = II()
for _ in range(t):
    a = II()
    L = [0] + LII()

    s = 'a' + I()
    dic = {}
    vis = [True] * (a + 1)
    k = []
    for idx in range(1, a + 1):
        if vis[idx]:
            tmp = set()
            cnt = 0
            while L[idx] not in tmp:
                tmp.add(L[idx])
                cnt += 1 if s[L[idx]] =='0' else 0
                vis[L[idx]] = False
                idx = L[idx]
            for i in tmp:
                dic[i] = cnt
    ans = sorted(dic.items(), key = lambda x: x[0])
    print(*[i[1] for i in ans])