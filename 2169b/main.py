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

t = II()
for _ in range(t):
    s = I()

    for i in range(len(s) - 1):
        if s[i] != '<' and s[i + 1] != '>':
            print(-1)
            break
    else:
        print(len(s) - min(s.count('<'), s.count('>')))