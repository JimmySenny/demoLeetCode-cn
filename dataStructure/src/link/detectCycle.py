#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#    def detectCycle(self, head: ListNode) -> ListNode:
    def detectCycle(self, head):
        fast = head
        slow = head
        while True:
            if not(fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        print("eq:", fast.val)
        fast = head
        step = 0
        while fast != slow:
            fast = fast.next
            slow = slow.next
            print(fast.val, slow.val)
            step += 1
        print("step:", step)
        return fast;

def main():
    link = ListNode(-1);
    n0 = ListNode(3);
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    link.next = n0
    n0.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n1

    s = Solution()
    print(s.detectCycle(link))

if __name__ == '__main__':
    main()
