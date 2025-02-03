# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())

count = 0
for _ in range(n):
    user_input = map(int, input().split())

    user_input = list(user_input)
    
    if user_input.count(1) > 1:
        count+=1


print(count)