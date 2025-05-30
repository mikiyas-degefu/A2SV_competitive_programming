# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempo_node = ListNode()
        self.head = tempo_node

        while list1 and list2:
            if list1.val <= list2.val:
                tempo_node.next = list1
                list1 = list1.next
            else:
                tempo_node.next = list2
                list2 = list2.next
            
            tempo_node = tempo_node.next 

        
        if list1:
            tempo_node.next = list1
        
        if list2:
            tempo_node.next = list2
        
        return self.head.next
        
