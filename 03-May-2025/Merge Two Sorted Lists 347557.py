# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        cur = new_head

        while list1 and list2:
            if list1.val <= list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return new_head.next