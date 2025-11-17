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
s = I()
t = I()
p = []
n = len(s)
f = 0
for i in range(n):
    if s[i] == t[i]:
        p.append(s[i])
    else:
        if f == 0:
            p.append(s[i])
        else:
            p.append(t[i])
        f = 1 - f
print(''.join(p) if f == 0 else "impossible")