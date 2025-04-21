# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode().next
        cur_dummy = dummy
        left_node = ListNode()
        left_head = left_node
        cur = head
        idx = 1

        while cur:
            if left <= idx:
                new_node = ListNode(cur.val)
                if left == idx:
                    cur_dummy = new_node
                new_node.next = dummy
                dummy = new_node

            else:
                left_node.next =  ListNode(cur.val)
                left_node = left_node.next
            if right == idx:
                cur = cur.next
                break
            idx+=1
            cur = cur.next

        left_node.next = dummy
        cur_dummy.next = cur

        return left_head.next
        
        
        