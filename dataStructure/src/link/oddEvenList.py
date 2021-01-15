#!/usr/bin/env python3

import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
#    def oddEvenList(self, head: ListNode) -> ListNode:
    def oddEvenList(self, head):
        if not head:
            return None
        head0 = ListNode(-1,head)
        prevOdd = head0
        headEven = None

        i = 1
        inode = head0.next
        while inode:
            print("i,inode", i,inode.val)
            if 1 == i:
                prevEven = inode
                headEven = inode.next
            
            if i % 2: #奇
                currOdd = inode
                prevOdd.next = currOdd
                prevOdd = currOdd
            else:
                currEven = inode
                prevEven.next = currEven
                prevEven = currEven
            if None == inode.next:
                break
            inode = inode.next
            i += 1
        # 这里不处理，奇数时会变成环形链表
        prevEven.next = None
        prevOdd.next = headEven
        return head0.next
    def iter(self,head):
        if not head:
            return None
        node = head
        while node.next:
            print(node.val, end='|')
            node = node.next
        print(node.val)

def main():
    s = Solution()
    n5 = ListNode(5)
    n4 = ListNode(4,n5)
    n3 = ListNode(3,n4)
    n2 = ListNode(2,n3)
    n1 = ListNode(1,n2)

    head = n1

    s.iter(head)
    n = s.oddEvenList(head)
    s.iter(n)

if __name__ == '__main__':
    main()
