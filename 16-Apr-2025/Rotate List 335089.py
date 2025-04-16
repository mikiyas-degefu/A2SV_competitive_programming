# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #if k is 0 nothing changed
        if k == 0:
            return head
        
        temp = head
        total = 0
        #count length of list
        while temp:
            total += 1
            temp = temp.next
        
        #if total is 0 nothing changed
        if total == 0:
            return head
        pos = k % total
        idx = total - pos

        print(pos)
        #if position is 0 nothing changed
        if pos == 0:
            return head

        new_head = None
        cur = head
        prev = None
        i = 0
        while i < idx:
            prev = cur
            cur = cur.next
            i+=1
        
        prev.next = None
        new_head = cur
        while cur.next:
            cur = cur.next
        
        cur.next = head
        return new_head
        