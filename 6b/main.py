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
a, b, s = I().split()
a = int(a)
b = int(b)

L = []
for _ in range(a):
    L.append(list(I()))
vis = set()
for i in range(a):
    for j in range(b):
        if L[i][j] == s:

            if i > 0 and L[i - 1][j] != s and L[i - 1][j] != '.':
                # print(L[i - 1][j], '.')
                vis.add(L[i - 1][j])
            if i < a - 1 and L[i + 1][j] != s and L[i + 1][j] != '.':
                # print(L[i + 1][j], '.')
                vis.add(L[i + 1][j])
            if j > 0 and L[i][j - 1] != s and L[i][j - 1] != '.':
                # print(L[i][j - 1], '.')
                vis.add(L[i][j - 1])
            if j < b - 1 and L[i][j + 1] != s and L[i][j + 1] != '.':
                # print(L[i][j + 1], '.')
                vis.add(L[i][j + 1])
# print(vis)
print(len(vis))