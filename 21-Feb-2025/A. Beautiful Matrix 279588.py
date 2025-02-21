# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

def find_one(li : list) -> list:
    for i in range(5):
        for j in range(5):
            if li[i][j] == 1:
                return[i,j]

b_max = []

for i in range(5):
    b_max.append( list(map(int, input().split())))

pos_one = find_one(b_max)

sum_i = pos_one[0] + 2
sum_j = pos_one[1] + 2

print(abs(pos_one[0] - 2) + abs(pos_one[1] - 2))