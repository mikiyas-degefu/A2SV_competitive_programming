# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())

a = []
b = []
c = []

for _ in range(N):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

dp = [[0]*3 for _ in range(N)]

# base case (day 0)
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1, N):
    dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2])  # swim today 
    dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2])  # bugs today
    dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1])  # homework today 


print(max(dp[N-1]))
