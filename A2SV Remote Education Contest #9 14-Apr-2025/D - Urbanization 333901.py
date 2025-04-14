# Problem: D - Urbanization - https://codeforces.com/gym/603156/problem/D

n, n1, n2 = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)
a1 = 0
a2 = 0
i = 0

if n2 > n1:
    n1, n2 = n2, n1

while i < n2:
    a1 += a[i]
    i += 1
while i < n2 + n1:
    a2 += a[i]
    i += 1

result = float((a1 / n2) + (a2 / n1))
formatted_value = "{:.8f}".format(result)
print(formatted_value)