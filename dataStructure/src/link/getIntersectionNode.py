#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pha, phb = headA, headB
        while pha != phb:
            pha = pha.next if pha.next else headB
            phb = phb.next if phb.next else headA
#            print("pha,phb:", pha.val, phb.val)
        return pha

def main():
    s = Solution()
    headA = ListNode(0)
    headB = ListNode(0)
    n0 = ListNode(10)
    n1 = ListNode(11)
    n2 = ListNode(12)
    n3 = ListNode(13)
    n4 = ListNode(14)
    n5 = ListNode(15)
    n6 = ListNode(16)
    n7 = ListNode(17)

    n6.next = n7
    n5.next = n6
    n4.next = n5
    n2.next = n4
    n1.next = n2
    n0.next = n1

    n3.next = n4

    headA.next = n0
    headB.next = n3

    print(s.getIntersectionNode(headA,headB))

if __name__ == '__main__':
    main()
