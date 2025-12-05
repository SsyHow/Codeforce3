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
_ = II()
L = LII()
ss = set(L)


k = sum(ss)
a = len(ss)
if a <= 2:
    print("YES")
elif k % a:
    print("NO")

else:
    k //= a
    s = set()

    for i in L:
        if (c := abs(i - k)) > 0:
            s.add(c)
    # print(s)
    print("NO" if len(s) > 1 else "YES")


