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
for _ in range(a):
    n = II()
    L = LII()
    cnt = [0] * (n + 1)
    for i in L:
        cnt[i] += 1

    ans = 0
    for s in range(2, 2 * n + 1):
        cur = 0
        for i in range(1, (s + 1) // 2):
            if (s - i > n):
                continue
            cur += min(cnt[i], cnt[s - i])
        if (s% 2 == 0):
            cur += cnt[s//2] // 2
        ans = max(ans, cur)
    print(ans)