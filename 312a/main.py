import sys

# input = lambda: sys.stdin.readline().rstrip()


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
# a = II()
# L = []
# for _ in range(a):
#     s = I()
#     x = s[:5]=="miao."
#     y = s[-5:]=="lala."
#     # print(x, y)
#     if (x and y) or (not x and not y):
#         L.append("OMG>.< I don't know!")
#     elif y:
#         L.append("Freda's")
#     else:
#         L.append("Rainbow's")
# print('\n'.join(L))

for _ in range(int(input())):
    s,m,l=input(),0,0
    if s[:5]=="miao.":m+=1
    if s[-5:]=="lala.":l+=1
    if l==m==1 or l==m==0:print("OMG>.< I don't know!")
    elif l:print("Freda's")
    elif m:print("Rainbow's")
