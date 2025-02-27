# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n,m = list(map(int, input().split()))

is_last = True
dot = '.' * (m-1)
for i in range(n):
    if i % 2 == 0:
        print('#' * m)
    else:
        if is_last:
            print(f"{dot}#")
            is_last = False
        else:
            print(f"#{dot}")
            is_last = True
            
            
        