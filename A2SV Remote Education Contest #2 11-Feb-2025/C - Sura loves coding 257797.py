# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
s = input().strip()

original = []

for i in range(n-1, -1, -1):
    char = s[i]

    if len(original) % 2 == 0:
        pos = len(original) // 2
    else:
        pos = len(original) // 2
    original.insert(pos, char)


original_word = ''.join(original)
print(original_word)
