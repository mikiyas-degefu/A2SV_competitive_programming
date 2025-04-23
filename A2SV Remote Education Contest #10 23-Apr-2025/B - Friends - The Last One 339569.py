# Problem: B - Friends - The Last One - https://codeforces.com/gym/604857/problem/B


def solve(n,m,a):
    if n > m: return "NO"

    a.sort(reverse=True)
    space = 0
    prev = 0


    for num in range(n):
        if prev - a[num] >= 0:
            space += a[num] + 1
        else:
            space += ((a[num] * 2) + 1)

        prev = a[num]
    
    if a[0] - a[-1] >= 0:
        space -= a[-1]
    if space > m:
        return "NO"
    else:
        return "YES"



t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n,m,a))