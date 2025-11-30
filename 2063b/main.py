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

for _ in range(II()):
    n, l, r = MII()
    l -= 1
    arr = LII()
    brr = arr[:l] + sorted(arr[l:])
    crr = sorted(arr[:r])[::-1] + arr[r:]
    print(min(sum(brr[l:r]), sum(crr[l:r])))