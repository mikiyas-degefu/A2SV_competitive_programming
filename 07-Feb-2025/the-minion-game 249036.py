# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    stuart = 0
    kevin = 0
    
    
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for i in range(len(string)):
        if string[i] not in vowel:
            stuart+=len(string[i:])
        else:
            kevin+=len(string[i:])
            
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart < kevin:
        print('Kevin', kevin)
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)