#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        mhead = ListNode(-1);
        prev = mhead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next;
            else:
                prev.next = l2;
                l2 = l2.next;
            prev = prev.next;

        prev.next = l1 if l1 is not None else l2;
        return mhead.next;
    def iter(self,head):
        pn = head
        num = 0
        while pn.next:
            pn = pn.next
            num += 1
            print(pn.val,end=',')
        print("num:",num)


def main():
    n9 = ListNode(9);
    n8 = ListNode(8,n9);
    n7 = ListNode(7,n8);
    n6 = ListNode(6,n7);
    n5 = ListNode(5,n6);
    n4 = ListNode(4,n5);
    n3 = ListNode(3,n4);
    n2 = ListNode(2,n3);
    n1 = ListNode(1,n2);

    m4 = ListNode(3.5)
    m3 = ListNode(2.5,m4)
    m2 = ListNode(1.5,m3)
    m1 = ListNode(0.5,m2)

    s = Solution();
    s.iter(n1)
    s.iter(m1)
    l = s.mergeTwoLists(n1,m1);
    s.iter(l)

if __name__ == '__main__':
    main();
