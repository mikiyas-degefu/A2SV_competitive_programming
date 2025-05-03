# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def geo_sum(s):
    if s == 0:
        return 1
    return 1/pow(3,s) + geo_sum(s-1)