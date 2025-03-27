# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = list(map(int, input().split()))


MAX_TEMP = 200000

prefix_freq = [0] * (MAX_TEMP + 2)
admissible = [0] * (MAX_TEMP + 1)

for _ in range(n):
    li, ri = list(map(int, input().split()))
    prefix_freq[li] += 1
    prefix_freq[ri+1] -= 1

#prefix sum
for i in range(1, MAX_TEMP + 1):
    prefix_freq[i] += prefix_freq[i-1]

#counting admissible
for i in range(1, MAX_TEMP + 1):
    if prefix_freq[i] >= k:
        admissible[i] = 1
    else:
        admissible[i] = 0

#prefix sum of admissible
for i in range(1, MAX_TEMP + 1):
    admissible[i] += admissible[i-1]

for _ in range(q):
    a,b = (list(map(int, input().split())))
    print(admissible[b] - admissible[a-1])