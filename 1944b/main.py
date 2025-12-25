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
from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[*map(int,input().split())]
    b,c=sorted(a[:n]),sorted(a[n:])
    d1,d2=Counter(b),Counter(c)
    m,p=[],[]
    for i in b:
        if d1[i]==1:m+=i,;
    for i in b:
        if d1[i]==2:m+=i,;
    for i in c:
        if d2[i]==1:p+=i,;
    for i in c:
        if d2[i]==2:p+=i,;
    while n>2*k+1:
        m.pop();m.pop()
        p.pop();p.pop()
        n-=2
    if n%2:print(*m[1:]);print(*p[1:]);continue
    print(*m);print(*p)