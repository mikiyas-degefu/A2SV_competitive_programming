# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        stack = []

        while head:
            stack.append(head.val)
            head = head.next
        
        l = 0
        r = len(stack) - 1

        while l <= r:
            if stack[l] != stack[r]:
                return False
            r-=1
            l+=1
        
        return True
        