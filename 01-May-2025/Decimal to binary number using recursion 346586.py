# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def decimal_to_binary(n):
    if n < 1:
        return
    return str(n % 2) + (decimal_to_binary(n//2) if n > 1 else '')