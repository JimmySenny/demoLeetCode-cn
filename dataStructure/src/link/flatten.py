#!/usr/bin/env python3

# Definition for singly-linked list.
class DLNode:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
#    def flatten(self, head: 'Node') -> 'Node':
    def flatten(self, head):
        if not head:
            return

        headNew = DLNode(-1,None,head,None)
        prev = headNew

        stack = []
        stack.append(head)
        while stack:
            curr = stack.pop()
            print("prev:", prev.val,prev.prev,prev.next,prev.child)
            print("curr:", curr.val,curr.prev,curr.next,curr.child)
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev.next = curr
            curr.prev = prev

            prev = curr
        headNew.next.prev = None
        self.iter(headNew.next)
        return headNew.next

    def iter(self,head):
        node = DLNode(0,None,head,None)
        while node.next:
            node = node.next
            print(node.val, end='|')
        print()
    def iterChild(self,head):
        node = DLNode(0,None,None,head)
        while node.child:
            node = node.child
            print(node.val, end='|')
        print()

def main():
    n32 = DLNode(12,None,None,None)
    n31 = DLNode(11,None,n32,None)

    n23 = DLNode(9,None,None,None)
    n22 = DLNode(8,None,n23,n31)
    n21 = DLNode(7,None,n22,None)

    n16 = DLNode(6,None,None,None)
    n15 = DLNode(5,None,n16,None)
    n14 = DLNode(4,None,n15,None)
    n13 = DLNode(3,None,n14,n21)
    n12 = DLNode(2,None,n13,None)
    n11 = DLNode(1,None,n12,None)
    
    n14.prev = n13
    n13.prev = n12
    n12.prev = n11

    n23.prev = n22
    n22.prev = n21

    n32.prev = n31

    s = Solution()

    s.iter(n11)
    s.iter(n21)
    s.iter(n31)
    s.iterChild(n13)
    s.iterChild(n22)
    l = s.flatten(n11)
    s.iter(l)
if __name__ == '__main__':
    main()
