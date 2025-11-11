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

s = sorted(s)
i = 0
while s[i] == '0':
    i += 1
    if i == len(s):
        break
else:
    s[0], s[i] = s[i], s[0]

print("OK" if ''.join(s) == t else "WRONG_ANSWER")