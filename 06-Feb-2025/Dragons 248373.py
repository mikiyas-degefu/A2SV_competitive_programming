# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = list(map(int, input().split()))

dragons = []

for _ in range(n):
    x,y = list(map(int, input().split()))

    dragons.append((x,y))

dragons.sort()

for x,y in dragons:
    if s > x:
        s += y
    else:
        print('NO')
        break
else:
    print('YES')