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
for _ in range(II()):
    a = I()
    b = I()

    n = len(a)
    m = len(b)
    ans = n + m

    for i in range(m):
        j = i
        for c in a:
            if j < m and c == b[j]:
                j += 1
        ans = min(ans, n + m - j + i)
    print(ans)