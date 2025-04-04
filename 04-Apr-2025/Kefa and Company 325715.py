# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n,d = list(map(int, input().split()))

friends = []

for _ in range(n):
    friends.append(list(map(int, input().split())))

friends.sort(key=lambda x: x[0])

left = 0
right = 0
max_friendship = 0
cur_friendship = 0

while right < n and left < n:
    if abs(friends[right][0] - friends[left][0]) < d:
        cur_friendship += friends[right][1]
        right += 1
    else:
        max_friendship = max(max_friendship, cur_friendship)
        cur_friendship -= friends[left][1]
        left += 1
max_friendship = max(max_friendship, cur_friendship)
print(max_friendship)