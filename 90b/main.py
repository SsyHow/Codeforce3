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
    L.append(list(I()))

K = []
for i in range(a):
    for j in range(b):
        k = L[i][j]
        f = False
        for m in range(b):
            if m != j and L[i][m] == k:
                K.append((i, m))
                f = True
        for n in range(a):
            if n != i and L[n][j] == k:
                K.append((n, j))
                f = True

        if f:
            K.append((i, j))
for x, y in K:
    L[x][y] = ''
print(''.join(''.join(i) for i in L))