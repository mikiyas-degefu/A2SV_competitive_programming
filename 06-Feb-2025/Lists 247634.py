# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    
    nums = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            nums.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(nums)
        elif command[0] == 'remove':
            nums.remove(int(command[1]))
        elif command[0] == 'append':
            nums.append(int(command[1]))
        elif command[0] == 'sort':
            nums.sort()
        elif command[0] == 'pop':
            nums.pop()
        else:
            nums.reverse()
