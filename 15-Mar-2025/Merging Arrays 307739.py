# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

result = []

i, j = 0, 0

while i < len(num1) or j < len(num2):
    if i < len(num1) and (j >= len(num2) or num1[i] <= num2[j]):
        result.append(num1[i])
        i += 1
    else:
        result.append(num2[j])
        j += 1

print(*result)
