# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = list(map(int, input().split()))

books =  list(map(int, input().split()))

l = 0
r = 0
time =  0
count = 0


while r < len(books) and l < len(books):
    if books[l] > t:
        if time - books[l] > 0:
            time -= books[l]
        else:
            time = 0
        l+=1
    else: 
        time += books[r] 
        if time <= t:
            count+=1
        else:
            time-=books[l]
            l+=1

    r+=1
    
print(count)  