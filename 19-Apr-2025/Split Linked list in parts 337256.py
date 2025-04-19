# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        temp = head

        #total size of linked list
        while temp:
            size += 1
            temp = temp.next
        
        split_size = size // k
        remaining_part = size % k

        cur = head
        res = [None] * k
        for i in range(k):
            dummy = ListNode(0)
            tail = dummy

            cur_size = split_size
            if remaining_part > 0:
                remaining_part -= 1
                cur_size += 1
            
            for j in range(cur_size):
                tail.next = ListNode(cur.val)
                tail = tail.next
                cur = cur.next
            res[i] = dummy.next
        
        return res
            

        



        