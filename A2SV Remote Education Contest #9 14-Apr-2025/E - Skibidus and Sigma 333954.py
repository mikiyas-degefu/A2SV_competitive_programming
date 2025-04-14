# Problem: E - Skibidus and Sigma - https://codeforces.com/gym/603156/problem/E

t = int(input())

for _ in range(t):
    #number if array and length of each array
    n, m = map(int, input().split())

    arrays = []

    for _ in range(n):
        x = list(map(int, input().split()))
        arrays.append(x)
    

    arrays.sort(key=lambda x: sum(x), reverse=True)

    extended_arrays = []
    for i in range(n):
        extended_arrays.extend(arrays[i])
    score = 0
    cur_sum = 0

    for x in extended_arrays:
        cur_sum += x
        score += cur_sum
    print(score)