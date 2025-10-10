# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

is_prime = []

def generate_primes():
    global is_prime
    if is_prime:
        return
    N = int(1e5) + 1
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    for i in range(2, N):
        if is_prime[i]:
            for j in range(2 * i, N, i):
                is_prime[j] = False

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        generate_primes()
        
        if is_prime[n] or is_prime[m]:
            return -1
        

        pq = [(n, n)]
        visited = set()
        
        while pq:
            steps, curr = heapq.heappop(pq)
            
            if curr in visited:
                continue
            visited.add(curr)
            
            if curr == m:
                return steps
            
            s = list(str(curr))
            for i in range(len(s)):
                original = s[i]
                

                if s[i] < '9':
                    s[i] = str(int(s[i]) + 1)
                    next_num = int(''.join(s))
                    if next_num not in visited and not is_prime[next_num]:
                        heapq.heappush(pq, (steps + next_num, next_num))
                    s[i] = original
                
                if s[i] > '0':
                    s[i] = str(int(s[i]) - 1)
                    next_num = int(''.join(s))
                    if next_num not in visited and not is_prime[next_num]:
                        heapq.heappush(pq, (steps + next_num, next_num))
                    s[i] = original
        
        return -1
