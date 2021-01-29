#!/usr/bin/env python3

from traversal import Solution as tr
from myBST import Solution as bst

class TreeNode:
    def __init__(self, val, count=1,left=None,right=None ):
        self.val = val
        self.left = None
        self.right = None
        self.count = count 
"""
若k等于cur.right.count+1 ，说明当前节点为所寻节点，直接返回；
若k小于cur.right.count+1 ，说明所寻节点大于当前值，在右子树中寻找第k大元素；
若k大于cur.right.count+1 ，说明所寻节点小于当前值，在左子树中寻找第k-(cur.right.count+1)大元素；
"""

class KthLargest:
    #def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insertIntoBST(self.root, num)

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val == val:
            return root
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        root.count += 1
        return root

    #def add(self, val: int) -> int:
    def add(self, val):
        self.root = self.insertIntoBST(self.root, val)
        return self.findKHelper(self.root, self.k).val
    #def findKHelper(self, cur:TreeNode, k)->TreeNode:
    def findKHelper(self, cur, k):
        curCount = 1
        if cur.right:
            curCount += cur.right.count
        if k == curCount:
            return cur
        elif k < curCount:
            return self.findKHelper(cur.right,k)
        else:
            return self.findKHelper(cur.left, k - curCount)

    def traversalflagiter(self,root,order):
        # 迭代 标志位迭代
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
                print(cur.count,end="|")
        print()
        return res
    
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def main():
    k = 3
    nums = [4, 5, 8, 2]
    obj = KthLargest(k, nums)
    print(obj.traversalflagiter(obj.root,"in"))
    print(obj.add(3))
    print(obj.traversalflagiter(obj.root,"in"))
    print(obj.add(6))
    print(obj.traversalflagiter(obj.root,"in"))
    print(obj.add(10))
    print(obj.traversalflagiter(obj.root,"in"))
    print(obj.add(9))
    print(obj.traversalflagiter(obj.root,"in"))
    print(obj.add(4))
    print(obj.traversalflagiter(obj.root,"in"))


if __name__ == '__main__':
    main()
