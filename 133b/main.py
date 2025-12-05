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
dic = {">" : 8,
    "<" : 9,
    "+" : 10,
    "-" : 11,
    "." : 12,
    "," : 13,
    "[" : 14,
    "]" : 15}

s = I()
ans = 0
for i in s:
    ans = ans * 16 + dic[i]
    ans = ans % (10 ** 6 + 3)
print(ans)
