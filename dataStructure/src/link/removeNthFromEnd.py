#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        # 增加哨兵节点，i避免删除长度为n的链表 倒数第n个节点
        node = ListNode(-1,head)
        ph1,ph2 = node,node,
        for i in range(n):
            if ph1.next:
                ph1 = ph1.next
                print(i,ph1.val, end='-')
            else:
                return None
        print("|")
        while ph1.next:
            ph1 = ph1.next
            ph2 = ph2.next
            print(ph2.val, end='=')
        print("|")
        print("p2:", ph2.val)

        prevd = ph2
        nextd = ph2.next.next
        prevd.next = nextd

        print("h:", node.next.val)
        return node.next
    def iter(self,head):
        pn = head
        num = 0
        while pn.next:
            pn = pn.next
            num += 1
            print(pn.val,end=',')
        print("num:",num)            

def main():
    s = Solution()
    """
    head = ListNode(-1)
    n5 = ListNode(5)
    n4 = ListNode(4,n5)
    n3 = ListNode(3,n4)
    n2 = ListNode(2,n3)
    n1 = ListNode(1,n2)
    n0 = ListNode(0,n1)

    head.next = n0
    """
    n1 = ListNode(2)
    n0 = ListNode(1,n1)
    head = ListNode(-1,n0)
    n = 2
    s.iter(head)
    head = s.removeNthFromEnd(n0,2)
    s.iter(head)

if __name__ == '__main__':
    main()
