#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def lowestCommonAncestorrecursion(self, root, p, q):
        return self.recursionLCA(root,p,q)
    def recursionLCA(self, root, p, q):
        """
        适用所有二叉树
        #递归法序遍历二叉树
        左边没找到右边也没找到。说明题目给的二叉树根本不包含 p 或 q，返回 nullptr。
        左边找到了右边也找到了。说明 p 和 q 分居在 root 的两侧，那么最低公共祖先为 root，返回 root。
        左边没找到右边找到了。说明 p 和 q 全都在 root 的右侧，加上我们在第一步就知道 root 不等于 p 也不等于 q，所以最低公共祖先在 root 的右子树，返回右子树。
        左边找到了右边没找到。说明 p 和 q 全都在 root 的左侧，加上我们在第一步就知道 root 不等于 p 也不等于 q，所以最低公共祖先在 root 的左子树，返回左子树。
        """
        if not root or root == p or root == q:
            return root
        nodeleft = self.recursionLCA(root.left,p,q)
        noderight = self.recursionLCA(root.right,p,q)
        if not nodeleft and not noderight: # 1
            return None
        if nodeleft and noderight:
            return root     # 2 
        if not nodeleft:    # 3
            return noderight
        if not noderight:   # 4
            return nodeleft

    def recursionLCA1(self, root, p, q):
        if not root:
            return False
        lson = self.recursionLCA1(root.left,p,q)
        rson = self.recursionLCA1(root.right,p,q)
        if((lson and rson)or((root.val == p.val or root.val == q.val) and (lson or rson))):
            print("LCA:",root.val)
            ans = root
        return lson or rson or (root.val==p.val or root.val==q.val)
    def lowestCommonAncestorrecursionBST(self, root, p, q):
        """
        适用二叉搜索树
        利用二叉搜索树特性，我们从根节点开始遍历；
        如果当前节点的值大于 p 和 q 的值，说明 p 和 q
          应该在当前节点的左子树，因此将当前节点移动到它的左子节点；
        如果当前节点的值小于 p 和 q 的值，说明 p 和 q
          应该在当前节点的右子树，因此将当前节点移动到它的右子节点；
        如果当前节点的值不满足上述两条要求，那么说明当前节点就是「分岔点」。
          此时p 和 q 要么在当前节点的不同的子树中，要么其中一个就是当前节点。
        """
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                break
        return cur


def main():
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n6 = TreeNode(6,None,n8)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3,n6,n7)
    n2 = TreeNode(2,n4,n5)
    n1 = TreeNode(1,n2,n3)

    root = n1

    s = Solution()
    lca = s.lowestCommonAncestorrecursion(root,n7,n8)
    if lca:
        print(lca.val)

if __name__ == '__main__':
    main()
