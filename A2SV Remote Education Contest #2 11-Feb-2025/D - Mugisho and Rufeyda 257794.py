# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n,t = list(map(int, input().split(' ')))

result = 10**(n-1)
if result % t == 0:
    print(result)
else:
    diff = t - (result % t)
    result+=diff
    result = str(result)
    if len(result) > n:
        print(-1)
    else:
        print(result)