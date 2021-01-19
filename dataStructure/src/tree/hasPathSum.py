#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    def hasPathSumRecusion(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSumRecusion(root.left, targetSum-root.val) or self.hasPathSumRecusion(root.right, targetSum - root.val)


    def hasPathSumBFS(self, root, targetSum):
        if not root:
            return False
        queue  = [root]
        queueSum = [root.val]
        while queue:
            cur = queue.pop(0)
            temp = queueSum.pop(0)
            if not cur.left and not cur.right:
                if temp == targetSum:
                    return True
                continue
            if cur.left:
                queue.append(cur.left)
                queueSum.append(cur.left.val + temp)
            if cur.right:
                queue.append(cur.right)
                queueSum.append(cur.right.val + temp)
        return False

def main():
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4,n8)
    n3 = TreeNode(3,n6,n7)
    n2 = TreeNode(2,n4,n5)
    n1 = TreeNode(1,n2,n3)

    root = n1

    s = Solution()
    print(s.hasPathSumRecusion(root, 8))
    print(s.hasPathSumBFS(root, 8))

    print(s.hasPathSumRecusion(root, 12))
    print(s.hasPathSumBFS(root, 12))

if __name__ == '__main__':
    main()
