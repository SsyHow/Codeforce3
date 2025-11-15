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
a, b = MII()

L = []
for _ in range(a):
    L.append(I())
ans = 0
for i in range(a):
    for j in range(b):
        if L[i][j] == 'W':
            f = False
            if i > 0 and L[i - 1][j] == 'P':
                f = True
            if j > 0 and L[i][j - 1] == 'P':
                f = True
            if i < a - 1 and L[i + 1][j] == 'P':
                f = True
            if j < b - 1 and L[i][j + 1] == 'P':
                f = True

            ans += 1 if f else 0
print(ans)