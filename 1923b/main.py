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
    N, K = MII()
    A = LII()
    P = LII()
    P = sorted([(abs(p), A[i]) for i, p in enumerate(P)])

    s = 0
    chk = 1
    for p, a in P:
        s += a
        if s > p * K:
            chk = 0
            break
    if chk: print("YES")
    else: print("NO")