# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    length = 0

    for i in range(n):
        if a[i] <= q:
            length += 1
        else:
            if length >= k:
                count += (length - k + 1) * (length - k + 2) // 2
            length = 0
    
    if length >= k:
        count += (length - k + 1) * (length - k + 2) // 2
    
    print(count)