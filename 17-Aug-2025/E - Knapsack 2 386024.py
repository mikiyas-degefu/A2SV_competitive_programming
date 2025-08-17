# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys
from functools import lru_cache

N, W = map(int, sys.stdin.readline().split())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

MAX_V = N * 1000  
INF = 10**18



@lru_cache(None)
def dp(i, val):
    if val == 0:
        return 0
    if i == 0:
        return INF 

    w, v = items[i-1]
    res = dp(i-1, val)  
    if val >= v:
        res = min(res, dp(i-1, val-v) + w)  
    return res

ans = 0
for val in range(MAX_V + 1):
    if dp(N, val) <= W:
        ans = val
print(ans)
