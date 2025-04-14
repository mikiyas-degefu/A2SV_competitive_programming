# Problem: A - The Rules of the Bus - https://codeforces.com/gym/603156/problem/A

t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    l = a[0] - 1
    r = a[0] + 1
    i = 1
    is_valid = True
    while i < n:
        if a[i] < l or a[i] > r:
            is_valid = False
            break
        l = min(l,a[i] - 1) 
        r = max(r,a[i] + 1)
        i += 1
    
    if is_valid:
        print("YES")
    else:
        print("NO")