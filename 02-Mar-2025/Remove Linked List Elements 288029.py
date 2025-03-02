# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        cur_head = ListNode()
        new_head = cur_head


        if head == None:
            return None
        
        while head != None:
            if head.val != val:
                if cur_head.val == 0:
                    cur_head.val = head.val
                elif cur_head.next == None:
                     cur_head.next = ListNode(val = head.val)
                     cur_head = cur_head.next
            head = head.next
        
        if new_head.val == 0:
            return None
        return new_head
