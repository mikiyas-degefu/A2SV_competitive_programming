# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
result = [0,0]

is_saraja = True
for i in range(n):
    max_card = max(cards[left], cards[right])
    if is_saraja:
        result[0] += max_card
    else:
        result[1] += max_card
    is_saraja = not is_saraja
    if cards[left] > cards[right]:
        left += 1
    else:
        right -= 1
print(result[0], result[1])