#!/usr/bin/env python3

# Definition for a binary tree node.
class Node:
    #def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    def __init__(self, val=0, left=None, right=None,next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    #def connect(self, root: 'Node') -> 'Node':
    def connectBFS(self, root):
    # 适用完美及一般二叉树
        if not root:
            return None
        queue = [root]
        while queue:
            #当前队列大小
            qlen = len(queue)
            #遍历这一层的所有节点 除最后一个节点外，其他节点next连接下一个节点
            for i in range(qlen):
                node = queue.pop(0)
                if i < qlen - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    def connectNext(self, root):
    # 适用完美二叉树
        if not root:
            return None
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # connect
                # 连接同一个父节点的两个子节点。它们可以通过同一个节点直接访问到
                head.left.next = head.right
                # connect
                # 父节点连接已建立的情况下，可以直接通过第一个父节点的 next 指针找到第二个父节点
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            #下一层
            leftmost = leftmost.left
        return root

    def connectLink(self, root):
    # 适用完美及一般二叉树
        if not root:
            return None
        # cur我们可以把它看做是每一层的链表
        cur = root
        while cur:
            #遍历当前层的时候，为了方便操作在下一层前面添加一个哑结点
            #（注意这里是访问当前层的节点，然后把下一层的节点串起来）
            dummy = Node(0)
            # pre表示访下一层节点的前一个节点
            pre = dummy
            while cur:
                if cur.left:
                    #如果当前节点的左子节点不为空，就让pre节点的next指向他，
                    #也就是把它串起来
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    #右节点同理
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            # 下一层串联后，让他赋值给cur
            cur = dummy.next;
        return root

    def traversalBFSlevel(self,root,order="pre"):
        if not root:
            return []
        queue = [root]
        res = [root.val]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                res.append(cur.left.val)
            if cur.right:
                queue.append(cur.right)
                res.append(cur.right.val)
        return res
    def traversalLevel(self,root):
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            lay, layval = [],[]
            for node in cur:
                layval.append(node.val)
                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            cur = lay
            res.append(layval)
        return res
    def traversalflagiter(self,root,order):
        res = []
        qs = [(0,root)]
        while qs:
            if "level" != order:
                flag, cur = qs.pop()
            else:
                flag, cur = qs.pop(0)
            if not cur:
                continue
            if 0 == flag:
                if "pre" == order:  # 根左右  re 右左根
                    qs.append((0,cur.right))
                    qs.append((0,cur.left))
                    qs.append((1,cur))
                if "in" == order:   # 左根右  re 右根左
                    qs.append((0,cur.right))
                    qs.append((1,cur))
                    qs.append((0,cur.left))
                if "post" == order: # 左右根  re 根右左
                    qs.append((1,cur))
                    qs.append((0,cur.right))
                    qs.append((0,cur.left))
                if "level" == order:# 层序 先上再下先左后右 queue left right 
                    qs.append((1,cur))
                    qs.append((0,cur.left))
                    qs.append((0,cur.right))
            else:
                if cur.next:
                    res.append([cur.val,cur.next.val])
                else:
                    res.append([cur.val,None])
        return res


def main():
    n8 = Node(8)
    n7 = Node(7)
    n6 = Node(6,None,n8)
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3,n6,n7)
    n2 = Node(2,n4,n5)
    n1 = Node(1,n2,n3)

    root = n1

    s = Solution()
    """
    print("before",s.traversalflagiter(root,"pre"))
    root1 = s.connectBFS(root)
    print("connect",s.traversalflagiter(root1,"pre"))
    print("before",s.traversalflagiter(root,"pre"))
    root2 = s.connectNext(root)
    print("connect",s.traversalflagiter(root2,"pre"))
    """
    print("before",s.traversalflagiter(root,"pre"))
    root3 = s.connectLink(root)
    print("connect",s.traversalflagiter(root3,"pre"))
if __name__ == '__main__':
    main()
