# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

n = int(input())
a = list(map(int, input().split()))

z_sorted = [0] * n

i = 0
r = n - 1
is_min = True
idx = 0
while idx < n:
    if is_min:
        if a[i] <= a[r]:
            z_sorted[idx] = a[i]
            i+=1
        else:
            z_sorted[idx] = a[r]
            r-=1
        is_min = False
    else:
        if a[i] <= a[r]:
            z_sorted[idx] = a[r]
            r-=1
        else:
            z_sorted[idx] = a[i]
            i+=1
        is_min = True
    
    idx+=1


print(*z_sorted)