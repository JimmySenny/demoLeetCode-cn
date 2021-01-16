#!/usr/bin/env python3

import time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Solution:
#    def rotateRight(self, head: ListNode, k: int) -> ListNode:
    def rotateRight(self, head, k):
        if not head:
            return head
        pNode = head
        n = 1
        while pNode.next:
            pNode = pNode.next
            n += 1
        linkTail = pNode
        print("n,linkTail", n,linkTail.val)
        k %= n
        if 0 == k:
            return head
        pNode = head
        newTail = head
        i = 0
        while pNode.next:
            if i < k:
                i += 1
                pNode = pNode.next
                continue
            i += 1
            pNode = pNode.next
            newTail = newTail.next
        if newTail == linkTail:
            newHead = head
        else:
            newHead = newTail.next
            newTail.next = None
            linkTail.next = head
        return newHead

    def iter(self,head):
        pn = ListNode(-1,head)
        num = 0
        while pn.next:
            pn = pn.next
            num += 1
            print(pn.val,end=',')
        print("iter:",num)


def main():
    n3 = ListNode(2);
    n2 = ListNode(1,n3);
    n1 = ListNode(0,n2);

    head = n1
    s = Solution();
    s.iter(head)
    s.iter(s.rotateRight(head,2))
    s.iter(head)
if __name__ == '__main__':
    main();
