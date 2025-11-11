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
dic = {'0' : 2, '1' : 7, '2': 2, '3': 3, '4' : 3, '5' : 4, '6': 2, '7': 5, '8': 1, '9' : 2}

ans = 1
for i in s:
    ans *= dic[i]
print(ans)