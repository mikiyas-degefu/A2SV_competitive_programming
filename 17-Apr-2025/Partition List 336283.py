# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        head_less = less
        greater = ListNode()
        head_greater = greater

        cur = head

        while cur:
            new_node = ListNode(cur.val)
            if cur.val < x:
                less.next = new_node
                less = less.next
            else:
                greater.next = new_node
                greater = greater.next
            cur = cur.next
        
        if less:
            less.next = head_greater.next
        
        return head_less.next




