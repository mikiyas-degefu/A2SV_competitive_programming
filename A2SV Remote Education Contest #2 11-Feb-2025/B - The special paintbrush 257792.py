# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    index_b = None
    last_b = 0

    for i,v in enumerate(s):
        if v == 'B' and index_b == None:
            index_b = i
        if v == 'B':
            last_b = i
    
    print(len(s[index_b:last_b+1]))
