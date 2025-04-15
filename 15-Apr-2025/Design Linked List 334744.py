# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        temp = self.head

        while temp:
            if i == index:
                return temp.val
            i+=1
            temp = temp.next
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        cur = self.head
        new_node = Node(val)

        if cur == None:
            self.head = new_node
            return 

        while cur.next != None:
            cur = cur.next
        
        cur.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
    
        if index == 0:
            self.addAtHead(val)
            return 
        
        prev = None
        cur = self.head
        new_node = Node(val)
        i = 0

        while i < index:
            if cur == None:
                return 
            prev = cur
            cur = cur.next
            i += 1
        new_node.next = cur
        prev.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        cur = self.head
        i = 0

        if self.head == None:
            return 
        if index == 0:
            self.head = self.head.next 

        else:
            while cur.next != None:
                if i == index:
                    break
                prev = cur
                cur = cur.next
                i += 1
            
            
            if i == index and cur.next == None:
                prev.next = None
            elif i == index:
                prev.next = cur.next
                del cur
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)