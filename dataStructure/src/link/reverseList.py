#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self,x,n=None):
        self.val = x;
        self.next = n;
class Solution:
#    def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if not head:
            return None;
        prev = None
        curr = head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev;            
    def reverseList2(self, head):
        if not head:
            return None;
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        return prev
    def iter(self,head):
        node = ListNode(-1,head)
        while node.next:
            print(node.val,end='|')
            node = node.next;
        print(node.val);
        print("----------")

def main():
    n5 = ListNode(5);
    n4 = ListNode(4,n5);
    n3 = ListNode(3,n4);
    n2 = ListNode(2,n3);
    n1 = ListNode(1,n2);
    head = n1

    s = Solution();
    s.iter(head);
    rehead = s.reverseList(head)
    s.iter(rehead)
    head = s.reverseList2(rehead)
    s.iter(head)

if __name__ == '__main__':
    main();
