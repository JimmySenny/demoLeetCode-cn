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
    #def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def sortedArrayToBST(self, nums):
        """
        中间点为根节点
        确定平衡二叉搜索树的根节点之后，
        其余的数字分别位于平衡二叉搜索树的左子树和右子树中，
        左子树和右子树分别也是平衡二叉搜索树，
        因此可以通过递归的方式创建平衡二叉搜索树。
        """
        return self.recursionArray2BST(nums,0,len(nums)-1)

    def recursionArray2BST(self, nums, left, right):
        if not nums or left > right:
            return None
        # 选择左中位数的数字作为根节点 
        #mid = (left + right) // 2 
        # 选择右中位数的数字作为根节点 
        mid = (left + right + 1) // 2
        print("left,right,mid", left,right,mid)

        rootNode = TreeNode(nums[mid])
        #numsLeft = nums[:mid]
        #numsRight = nums[mid+1:]

        if 0 == mid:
            rootNode.left = None
        else:
            rootNode.left = self.recursionArray2BST(nums,left, mid-1)
        if right == mid:
            rootNode.right = None
        else:
            rootNode.right = self.recursionArray2BST(nums,mid+1,right)

        return rootNode

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
    nums = [-10,-3,0,5,9]

    s = Solution()

    timeStamp1 = time.time()
    root = s.sortedArrayToBST(nums)
    timeStamp2 = time.time()
    print(timeStamp2 - timeStamp1)
    
    print("pre", s.traversalflagiter(root, "pre"))
    print("in", s.traversalflagiter(root, "in"))
    print("post", s.traversalflagiter(root, "post"))
    print("level", s.traversalflagiter(root, "level"))


if __name__ == '__main__':
    main()
