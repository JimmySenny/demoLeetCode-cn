#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Solution:
#    def isPalindrome(self, head: ListNode) -> bool:
    def isPalindrome(self, head):
        #1.快指针走到末尾，慢指针刚好到中间
        #2.其中慢指针将前半部分反转(可以和第一步结合处理)
        #3.比较
        #4.比较同时再反转 恢复链表
        if not head or not head.next:
            return True
        isP = True
        #快慢指针找到左中位及右中位

        # 1 2
        fast = slow = head
        prev = None
        curr = slow
        while fast and fast.next:
            print("fast,slow:",fast.val,slow.val)
            curr = slow

            slow = slow.next
            fast = fast.next.next

            curr.next = prev
            prev = curr
        print("prev:")
        self.iter(prev)
        
        midleft = slow
        print("slow:")
        self.iter(slow)
        if fast:
            slow = slow.next
        print("slow2:")
        self.iter(slow)

        #逆序的前半部分和顺序的后半部分比较 同时对逆序的前半部分再逆序，恢复链表
        reprev = midleft
        while prev and slow:
            if prev.val != slow.val:
                isP = False
            temp = prev

            prev = prev.next
            slow = slow.next

            temp.next = reprev
            reprev = temp
        print("prev:")
        self.iter(reprev)
        return isP

    def iter(self,head):
        pn = ListNode(-1,head)
        num = 0
        while pn.next:
            pn = pn.next
            num += 1
            print(pn.val,end=',')
        print("num:",num)


def main():
#    n6 = ListNode(6);
#    n5 = ListNode(5,n6);
#    n5 = ListNode(1)
#    n4 = ListNode(2,n5);
#    n3 = ListNode(1);
    n2 = ListNode(1);
    n1 = ListNode(1,n2);

    s = Solution();
    s.iter(n1)
    print(s.isPalindrome(n1))

if __name__ == '__main__':
    main();
