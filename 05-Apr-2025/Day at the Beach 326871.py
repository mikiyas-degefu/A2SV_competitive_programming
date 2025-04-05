# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

n = int(input())
h = list(map(int, input().split()))

left_max = [0] * n
right_min = [0] * n


left_max[0] = h[0]
for i in range(1, n):
    left_max[i] = max(left_max[i-1], h[i])


right_min[n-1] = h[n-1]
for i in range(n-2, -1, -1):
    right_min[i] = min(right_min[i+1], h[i])

count = 0
for i in range(n - 1):
    if left_max[i] <= right_min[i + 1]:
        count += 1
print(count + 1)