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
n, k = MII()
L = LII()



if sum(L) % k > 0:
    print("No")
else:
    x = sum(L) // k

    ans = []
    tmp = 0
    cnt = 0
    for i in L:
        tmp += i
        cnt += 1
        if tmp == x:
            ans.append(cnt)
            tmp = cnt = 0
        elif tmp > x:
            print("No")
            break
    else:
        print("Yes")
        print(*ans)
