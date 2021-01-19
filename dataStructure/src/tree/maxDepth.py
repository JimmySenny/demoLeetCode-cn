#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def maxDepth(self, root: TreeNode) -> int:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            heightLeft = self.maxDepth(root.left)
            heightRight = self.maxDepth(root.right)
            return max(heightLeft, heightRight) + 1

        return res[::-1]
    def maxDepthLevel(self,root):
        res = 0
        if not root:
            return res
        cur = [root]
        while cur:
            lay, layval = [],[]
            for node in cur:
                layval.append(node.val)
                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            cur = lay
            res += 1
        return res;
    def maxDepthBFS(self,root):
        res = 0
        qs = [root]
        while qs:
            size = len(qs)
            for i in range(size):
                cur = qs.pop(0)
                if cur.left:
                    qs.append(cur.left)
                if cur.right:
                    qs.append(cur.right)
            res += 1
        return res
    def maxDepthDFS(self,root):
        stackTree= [root]
        stackDepth = [0]
        maxDepth = 0
        while stackTree:
            cur = stackTree.pop()
            temp = stackDepth.pop()
            maxDepth = max(maxDepth, temp)
            if cur.left:
                stackTree.append(cur.left)
                stackDepth.append(temp + 1)
            if cur.right:
                stackTree.append(cur.right)
                stackDepth.append(temp + 1)
        return maxDepth

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
    print(s.maxDepth(root))
    print(s.maxDepthLevel(root))
    print(s.maxDepthBFS(root))

if __name__ == '__main__':
    main()
