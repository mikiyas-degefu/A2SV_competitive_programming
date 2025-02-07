# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())

gifts = [0] * n

list_of_friends = input().split()

for i,fr in enumerate(list_of_friends):
    gifts[int(fr)-1] = i+1

print(*gifts)