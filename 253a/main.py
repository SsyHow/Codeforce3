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
with open("input.txt", 'r') as f:
    a, b = map(int, f.readline().split())
    with open("output.txt", 'w') as g:

        if a >= b:
            print("BG" * b + 'B' * (a - b), file=g)
        else:
            print("GB" * a + "G" * (b - a), file=g)
