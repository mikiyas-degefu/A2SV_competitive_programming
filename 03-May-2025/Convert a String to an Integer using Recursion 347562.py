# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def str_to_int(s):
    n = len(s)
    if n == 0:
        return 0
    power = pow(10,n-1)
    
    
    return (power * int(s[0])) + str_to_int(s[1:n])