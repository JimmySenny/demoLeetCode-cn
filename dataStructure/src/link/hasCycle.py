#!/usr/bin/env python

class ListNode:
    def __init__(self, x ):
        self.val = x;
        self.next = None;

class Solution:
#    def hasCycle(self, head: ListNode) -> bool:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next: 
            slow = slow.next;
            fast = fast.next.next;
            if(fast == slow):
                return True;
        return False;

def main():
    head = ListNode(-1);
    n0 = ListNode(3);
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    head.next = n0
    n0.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n1
#    n3.next = None;
#    n1.next = n0;

    s = Solution();
    print(s.hasCycle(head));

if __name__ == '__main__':
    main();
