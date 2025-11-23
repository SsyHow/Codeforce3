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
n, m = MII()
dic = {}
dicp ={}
ans1 = ans2 = 0
for _ in range(n):
    x, y = MII()
    dic[y] = dic.get(y, 0) + 1
    dicp[(x, y)] = dicp.get((x,y), 0) + 1

# print(dic)
# print(dicp)
for _ in range(m):
    x, y = MII()
    if y in dic and dic[y] > 0:
        ans1 += 1
        dic[y] -= 1
    if (x, y) in dicp and dicp[(x, y)] > 0:
        ans2 += 1
        dicp[(x, y)] -= 1

print(ans1, ans2)
