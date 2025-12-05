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
    b = II()
    s = I()
    l1 = []
    l2 = []
    f = True
    for i in s:
        if i == '2':
            if f:
                l1.append(1)
                l2.append(1)
            else:
                l1.append(0)
                l2.append(2)
        elif i == '1':
            if f :
                l1.append(1)
                l2.append(0)
            else:
                l1.append(0)
                l2.append(1)
            f = False
        else:
            l1.append(0)
            l2.append(0)
    print(*l1, sep = '')
    print(*l2, sep = '')
