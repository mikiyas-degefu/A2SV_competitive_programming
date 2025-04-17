# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur_node = dummy_node
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            cur_sum = v1 + v2 + carry

            carry, cur_sum = divmod(cur_sum, 10)
            cur_node.next = ListNode(cur_sum)
            cur_node = cur_node.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        
        return dummy_node.next

        

        


            

            


        