# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = Counter(nums)

        sorted_frq = sorted(frq.items(), key=lambda item: item[1], reverse = True)

        ans = []
        for key, val in sorted_frq:
            if len(ans) == k:
                break
            ans.append(key)
        

        return ans