#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

class Solution:
#    def removeElements(self, head: ListNode, val: int) -> ListNode:
    def removeElements(self, head, val):
        if not head:
            return None
        node = ListNode(-1,head)
        fast = head
        slow = node
        while fast:
            if fast.val == val:
                slow.next = fast.next
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        return node.next

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
    n6 = ListNode(0)
    """
    n5 = ListNode(5,n6)
    n4 = ListNode(4,n5)
    n3 = ListNode(3,n4)
    n2 = ListNode(2,n3)
    n1 = ListNode(1,n2)
    n0 = ListNode(0,n1)
    """
    head = n6
    s.iter(head)
    n = s.removeElements(head,0)
    s.iter(n)

if __name__ == '__main__':
    main()
