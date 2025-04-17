# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = defaultdict(int)
        cur = head
        prev = None

        while cur:
            if cur.val not in stack:
                stack[cur.val] = None
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next
        
        return head
