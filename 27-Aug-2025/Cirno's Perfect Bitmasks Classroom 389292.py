# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(data[idx]); idx += 1
        if x == 1:
            out.append("3")
            continue
        L = x & -x
        if L != x:
            out.append(str(L))
        else:
            out.append(str(x + 1))
    sys.stdout.write("\n".join(out))

solve()
