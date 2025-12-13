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
n, res, x = MII()
L = LII()

L.sort()

prev = L[0]
cnt = 0
k = []
for i in L:
    if i - prev <= x:
        prev = i
        continue
    else:
        k.append(i - prev)
        prev = i
k.sort(reverse=True)

while k and res >= 0:
    if (k[-1] - 1) // x <= res:
        res -= (k[-1] - 1) // x
        k.pop()
    else:
        break
print(len(k) + 1)