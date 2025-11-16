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
a = II()
for _ in range(a):
    n, k = MII()
    s = I()

    start = unk = 0
    end = n - 1
    for i in s:
        if i == '0':
            start += 1
        elif i == '1':
            end -= 1
        else:
            unk += 1

    L = ["+"] * n
    for i in range(start ):
        L[i] = '-'
    for i in range(n - 1, end, -1):
        L[i] = '-'
    # print(end, start)
    if unk == end - start + 1:
        print(*(['-'] * n), sep = '')
    else:

        while unk > 0 and start <= end:
            L[start] = '?'
            L[end] = '?'
            start += 1
            end -= 1
            unk -= 1


        print(*L, sep = '')