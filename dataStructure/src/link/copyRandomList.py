#!/usr/bin/env python3

# Definition for singly-linked list.
class Node:
#    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
#    def copyRandomList(self, head: 'Node') -> 'Node':
    def copyRandomList(self, head):
        if not head:
            return head
        # 创建一个哈希表，key是原节点，value是新节点
        dic = dict()
        pNode = head
        # 将原节点放入哈希表中 同时创建新节点
        while pNode:
            newNode = Node(pNode.val,None,None)
            dic[pNode] = newNode
            pNode = pNode.next
        # 遍历原链表，设置新节点的next和random
        pNode = head
        while pNode:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点]]
            if pNode.next:
                dic[pNode].next = dic[pNode.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点
            if pNode.random:
                dic[pNode].random = dic[pNode.random]
            pNode = pNode.next
        return dic[head]

    def iter(self,head):
        node = head
        while node:
            print(node.val, end='|')
            node = node.next
        print()
    def iterRandom(self,head):
        node = head
        while node:
            if node.random:
                print(node.random.val, end='|')
            else:
                print("None", end='|')
            node = node.next
        print()

def main():
    n5 = Node(1,None,None)
    n4 = Node(10,n5,None)
    n3 = Node(11,n4,None)
    n2 = Node(13,n3,None)
    n1 = Node(7,n2,None)

    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    head = n1

    s = Solution()
    s.iter(head)
    s.iterRandom(head)
    l = s.copyRandomList(head)
    s.iter(l)
    s.iterRandom(l)
if __name__ == '__main__':
    main()
