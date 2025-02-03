# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())

for _ in range(n):
    word = input()

    if len(word) > 10:
        result = word[0] + str(len(word[1:-1])) + word[-1]
        print(result)
    else:
        print(word)