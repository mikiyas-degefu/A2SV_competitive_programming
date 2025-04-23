# Problem: C - The big bang theory -  The Stockholm Syndrome - https://codeforces.com/gym/604857/problem/C

def solve(n,a):
    a.sort()
    prev = 0
    diff = 0
    min_val = a[0]

    for i in range(n):
        diff = a[i] - prev - 1
        if diff > 0 and a[i] - diff > 0:
            a[i] = a[i] - diff
        if prev - a[i] > 1:
            return prev + 1
        prev = a[i]

    return prev + 1

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))