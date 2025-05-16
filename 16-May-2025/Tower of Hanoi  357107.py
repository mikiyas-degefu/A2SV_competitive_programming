# Problem: Tower of Hanoi  - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

f n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
