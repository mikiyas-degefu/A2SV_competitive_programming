# Problem: A - How i met your mother - Last Forever - https://codeforces.com/gym/604857/problem/A

from collections import Counter
n = int(input())
a = input()

frq = Counter(a)

result = ''

if 'n' in frq:
    print("1 " * frq['n'] , end='')

if 'z' in frq:
    print("0 " * frq['z'] )