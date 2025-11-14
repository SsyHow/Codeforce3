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
a = 3
if s[0] == 'h':
    a = 4

b = s.find('ru',a + 1)
if b + 2 >= len(s):
    print(s[:a], "://", s[a:b], '.ru', sep = '')
else:
    print(s[:a], "://", s[a:b], '.ru/', s[b+2:], sep = '')