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
L = LII()
M = LII()
cnt = 0
vis = set(L).union(set(M))
for i in range(a):
    for j in range(a):
        if L[i] ^ M[j] in vis:
            cnt += 1

print("Karen" if cnt & 1 == 0 else "Koyomi")