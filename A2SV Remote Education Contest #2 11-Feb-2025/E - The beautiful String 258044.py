# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

n = int(input())

for _ in range(n):
    s = input()   
    seq = '1100'
    count = s.count(seq)
    lst_word = list(s)

    q_size = int(input())
    for _ in range(q_size):
        i,v = input().split()
        i = int(i) - 1

        bf_change = "".join(lst_word[max(0,i-3) : i+4]).count(seq)
        lst_word[i] = v
        af_change = "".join(lst_word[max(0,i-3) : i+4]).count(seq)

        count+=af_change - bf_change

        print('YES' if count > 0 else 'NO')