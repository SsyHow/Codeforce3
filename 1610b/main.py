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


def check(x):
    M = []
    for i in L:
        if i != x:
            M.append(i)
    bb = len(M)
    k = bb // 2
    for i in range(k):
        if M[i] != M[bb - i - 1]:
            return False
    return True
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    L = LII()
    k = b // 2
    for i in range(k):
        if L[i] != L[b - i - 1]:
            print("YES" if check(L[i]) or check(L[b - i - 1]) else "NO")
            break
    else:
        print("YES")