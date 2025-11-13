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
    a, b = MII()

    if a == b:
        print(0)

    elif (1 << a.bit_length()) - 1 < b:
        print(-1)

    else:
        print(2)
        print(((1 << a.bit_length()) - 1) ^ a , ((1 << a.bit_length()) - 1) ^ b)
