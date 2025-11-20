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
n, s = MII()
lands = []
for _ in range(n):
    h, m = MII()
    lands.append(h * 60 + m)

if lands[0] >= s + 1:
    print(0, 0)
else:
    f = True
    for i in range(n - 1):
        L = lands[i]
        R = lands[i + 1]

        if f and R - L >= 2 * s + 2:
            t = L + s + 1
            print(t // 60, t % 60)

            f = False
    if f:
        t = lands[-1] + s + 1
        print(t // 60, t % 60)



