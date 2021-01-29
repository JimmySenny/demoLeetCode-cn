#!/usr/bin/env python3

from traversal import Solution as tr

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    def searchBSTRe(self, root, val):
        return self.recursionSearchBST(root,val)
    def recursionSearchBST(self,root,val):
        if not root:
            return root
        if root.val == val:
            return root
        elif root.val > val:
            return self.recursionSearchBST(root.left, val)
        else:
            return self.recursionSearchBST(root.right, val)
    def searchBSTIter(self, root, val):
        while root:
            if root.val == val:
                break
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root
    #def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    def insertIntoBSTRe(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val == val:
            return root
        elif root.val > val:
            root.left = self.insertIntoBSTRe(root.left, val)
        else:
            root.right = self.insertIntoBSTRe(root.right, val)
        return root
    def insertIntoBSTIter(self, root, val):
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            # 如果当前节点cur的值大于val，说明val值应该插入到当前节点cur的左子树，
            # 否则就插入到当前节点cur的右子树
            # 增加特例判断 若一致则返回 不新增节点
            if cur.val == val:
                break
            elif cur.val > val:
                # 如果左子节点不为空，就继续往下找
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
                pass
            pass
        return root
    #def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    def deleteNodeRe(self, root, key):
        return self.recursiondeleteBST(root,key)
    def recursiondeleteBST(self,root,key):
        if not root:
            return None
        if root.val > key:
            root.left = self.recursiondeleteBST(root.left, key)
        elif root.val < key:
            root.right = self.recursiondeleteBST(root.right, key)
        else: # root.val == key:
            # 叶子节点
            if not root.left and not root.right:
                root = None
            elif root.right:
                # 存在右子节点，则将右树中的最小的叶子节点赋值给当前节点并将其删除
                # 即右树中的最左叶子节点删除
                rightMin = root.right
                while rightMin.left:
                    rightMin = rightMin.left
                root.val = rightMin.val # 值交换
                #递归删除下一个节点
                root.right = self.recursiondeleteBST(root.right, root.val)
            else:
                leftMax = root.left
                while leftMax.right:
                    leftMax = leftMax.right
                root.val = leftMax.val 
                root.left = self.recursiondeleteBST(root.left, root.val)

        # 必须返回root节点
        return root

def main():
    n22 = TreeNode(3)
    n21 = TreeNode(1)
    n11 = TreeNode(2,n21,n22)
    n12 = TreeNode(7)
    n01 = TreeNode(4,n11,n12)
    root = n01

    t = tr()
    s = Solution()

    print("iter-in",t.traversalflagiter(root,"in"))
    print(s.searchBSTRe(root,2).val)
    print(s.searchBSTIter(root,3).val)
    print("iter-in",t.traversalflagiter(s.insertIntoBSTRe(root,9),"in"))
    print("iter-in",t.traversalflagiter(s.insertIntoBSTIter(root,6),"in"))
    print("iter-in",t.traversalflagiter(s.insertIntoBSTIter(root,5),"in"))
    print("iter-in",t.traversalflagiter(s.insertIntoBSTIter(root,8),"in"))
    s.deleteNodeRe(root,7)
    print("iter-in",t.traversalflagiter(root,"in"))
    s.deleteNodeRe(root,4)
    print("iter-in",t.traversalflagiter(root,"in"))

    n1 = TreeNode(0)
    print("iter-in",t.traversalflagiter(n1,"in"))
    tmp = s.deleteNodeRe(n1,0)
    print("iter-in",t.traversalflagiter(tmp,"in"))

if __name__ == '__main__':
    main()
