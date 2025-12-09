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
for i in range(II()):
    n,m=MII()
    s=I()
    if '1'*m in s:
        print('NO')
        continue
    l=[0]*n
    maxi=n
    for i in range(n):
        if s[i]=="0":
            l[i]=maxi
            maxi-=1
    mini=1
    for i in range(n):
        if s[i]=='1':
            l[i]=mini
            mini+=1
    print('YES')
    print(*l)