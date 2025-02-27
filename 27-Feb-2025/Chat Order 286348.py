# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())

chats = {}
for chat in range(n):
    ch = input()
    if ch in chats:
        chats.pop(ch)
    chats[ch] = None

reverse = reversed(chats.keys() )
print("\n".join(reverse))
