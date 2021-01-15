#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
#    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
#        l1 = self.reverseLink(l1)
#        l2 = self.reverseLink(l2)
        self.iter(l1)
        self.iter(l2)
        carry = 0
        l = ListNode(-1)
        curr = l
        while l1 or l2 or carry:
            if l1:
                n1,l1 = l1.val,l1.next 
            else:
                n1 = 0
            if l2:
                n2,l2 = l2.val,l2.next
            else:
                n2 = 0
            
            n = n1 + n2 + carry
            carry = 1 if n >= 10 else 0
            node = ListNode(n%10)
            print(node.val,end='--')
            curr.next = node
            curr = curr.next
        print()
        return self.reverseLink(l.next)
    def reverseLink(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev

    def iter(self,head):
        node = ListNode(0,head)
        while node.next:
            node = node.next
            print(node.val, end='|')
        print()

def main():
    n14 = ListNode(9)
    n13 = ListNode(4,n14)
    n12 = ListNode(6,n13)
    n11 = ListNode(5,n12)
    n23 = ListNode(9)
    n22 = ListNode(4,n23)
    n21 = ListNode(2,n22)
    l1 = n11
    l2 = n21

    s = Solution()
    l = s.addTwoNumbers(l1,l2)
    s.iter(l)
if __name__ == '__main__':
    main()
