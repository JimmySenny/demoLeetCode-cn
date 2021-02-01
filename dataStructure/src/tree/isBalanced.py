#!/usr/bin/env python3

import time
from serialize import Codec as iSerialize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #def isBalanced(self, root: TreeNode) -> bool:
    def isBalancedUp2Down(self, root):
        # 自顶向下的递归
        """
        height 用于计算二叉树中的任意一个节点 p 的高度
        有了计算节点高度的函数，即可判断二叉树是否平衡。
        具体做法类似于二叉树的前序遍历，即对于当前遍历到的节点，
        首先计算左右子树的高度，如果左右子树的高度差是否不超过 1，
        再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalancedUp2Down(root.left) and self.isBalancedUp2Down(root.right)
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1

    def isBalancedDow2Up(self, root):
        # 自底向上的递归
        """
        由于上述自顶向下的递归存在重复调用的方式，考虑自底向上递归
        通过后续遍历方式，可有效降低重复递归次数
        """
        #return self.height2(root)
        return self.height2(root) >= 0
    def height2(self, root):
        if not root:
            return 0
        heightLeft = self.height2(root.left)
        heightRight = self.height2(root.right)
        if -1 == heightLeft or -1 == heightRight or abs(heightLeft - heightRight) > 1:
            return -1
        else:
            return max(heightLeft, heightRight) + 1

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
                res.append(cur.val)
        return res


def main():

    serializeData = "3,9,20,None,None,15,7,"

    c = iSerialize()
    root = c.deserializeBFS(serializeData)

    s = Solution()
    print("pre", s.traversalflagiter(root, "pre"))
    print("in", s.traversalflagiter(root, "in"))
    print("post", s.traversalflagiter(root, "post"))
    print("post", s.traversalflagiter(root, "level"))

    timeStamp1 = time.time()
    print(s.isBalancedUp2Down(root))
    timeStamp2 = time.time()
    print(timeStamp2 - timeStamp1)

    timeStamp1 = time.time()
    print(s.isBalancedDow2Up(root))
    timeStamp2 = time.time()
    print(timeStamp2 - timeStamp1)

    


if __name__ == '__main__':
    main()
