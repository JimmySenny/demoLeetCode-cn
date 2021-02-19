#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def isSymmetric(self, root: TreeNode) -> bool:
    def subRecusion(self, rootleft, rootright):
        if not rootleft and not rootright:
            return True
        if not rootleft or not rootright:
            return False
        return rootleft.val == rootright.val and self.subRecusion(rootleft.left, rootright.right) and self.subRecusion(rootleft.right, rootright.left)
    def isSymmetricRecusion(self, root):
        if not root:
            return True
        else:
            return self.subRecusion(root.left, root.right)
    def isSymmetricIter(self,root):
        if not root:
            return True
        if self.traversalIter(root.left,"pre") == self.traversalIter(root.right,"prere"):
            return True
        else:
            return False
    def traversalIter(self,root,order):
        res = []
        stack = [(0,root)]
        while stack:
            flag, cur = stack.pop()
            if not cur:
                res.append(None)
                continue
            if 0 == flag:
                if "pre" == order:
                    stack.append((0,cur.right))
                    stack.append((0,cur.left))
                    stack.append((1,cur))
                if "prere" == order:
                    stack.append((0,cur.left))
                    stack.append((0,cur.right))
                    stack.append((1,cur))
            else:
                res.append(cur.val)
        print(res)
        return res


def main():
    n8 = TreeNode(8)
    n7 = TreeNode(4)
    n6 = TreeNode(5)
    n5 = TreeNode(5)
    n4 = TreeNode(4,n8)
    n3 = TreeNode(2,n6,n7)
    n2 = TreeNode(2,n4,n5)
    n1 = TreeNode(1,n2,n3)

    root = n1

    s = Solution()
    print(s.isSymmetricRecusion(root))
    print(s.isSymmetricIter(root))

    n4.left = None
    print(s.isSymmetricRecusion(root))
    print(s.isSymmetricIter(root))


if __name__ == '__main__':
    main()
