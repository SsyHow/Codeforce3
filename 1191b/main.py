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


t = input().strip().split()

m = 3

for i in range(1, 8):
    for j in 'mps':
        r = 3
        if str(i) + j in t: r -= 1
        if str(i + 1) + j in t: r -= 1
        if str(i + 2) + j in t: r -= 1
        m = min(m, r)

print(min(m, len(set(t)) - 1))