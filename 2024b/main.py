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
    n, k = MII()
    L = LII()
    L.sort()

    i = 0
    x = ans = 0
    prev = 0
    while i < n:
        x += (L[i] - prev)* (n - i)
        if x >= k:
            x -= (L[i] - prev) * (n - i)
            ans += k - x
            break
        ans += (L[i] - prev) * (n - i) + 1

        prev = L[i]
        i += 1

    print(ans)

