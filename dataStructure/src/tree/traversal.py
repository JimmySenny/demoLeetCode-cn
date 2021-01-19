#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def traversal(self, root: TreeNode) -> List[int]:
    def traversalRecursion(self, root,order="pre"):
        if not root:
            return []
        if "pre" == order:
            return [root.val] + self.traversalRecursion(root.left,order) + self.traversalRecursion(root.right,order)
        elif "in" == order:
            return self.traversalRecursion(root.left,order) + [root.val] + self.traversalRecursion(root.right,order)
        elif "post" == order:
            return self.traversalRecursion(root.left,order) + self.traversalRecursion(root.right,order) + [root.val]
        else:
            return None
    def subrecursion(self,curr,res,order):
        if not curr:
            return []
        if "pre" == order: 
            res.append(curr.val)
            self.subrecursion(curr.left,res,order)
            self.subrecursion(curr.right,res,order)
        elif "in" == order:
            self.subrecursion(curr.left,res,order)
            res.append(curr.val)
            self.subrecursion(curr.right,res,order)
        elif "post" == order:
            self.subrecursion(curr.left,res,order)
            self.subrecursion(curr.right,res,order)
            res.append(curr.val)
        else:
            return None
    def traversalRecursion2(self, root,order="pre"):
        res = []
        self.subrecursion(root,res,order)
        return res
    def traversalDFS(self,root,order="pre"):
        res = []
        stack = []
        cur = root
        #前序
        if "pre" == order:
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                cur = cur.right
            return res
        #中序
        if "in" == order:
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res
        #后序
        if "post" == order:
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.right
                cur = stack.pop()
                cur = cur.left
            return res[::-1]
    def traversalDFSpre(self,root,order="pre"):
        if not root:
            return []
        res = []
        stack= [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
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
    def traversalDFSpost(self,root,order="post"):
        if not root:
            return []
        res = []
        stack= [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            res.append(cur.val)
        return res[::-1]
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
    print("pre")
    print("traversalRecursion",s.traversalRecursion(root,"pre"))
    print("traversalRecursion2",s.traversalRecursion2(root,"pre"))
    print("traversalDFS",s.traversalDFS(root,"pre"))
    print("traversalDFSpre",s.traversalDFSpre(root,"pre"))
    print("traversalflagiter",s.traversalflagiter(root,"pre"))
    print("in")
    print("traversalRecursion",s.traversalRecursion(root,"in"))
    print("traversalRecursion2",s.traversalRecursion2(root,"in"))
    print("traversalDFS",s.traversalDFS(root,"in"))
    print("traversalflagiter",s.traversalflagiter(root,"in"))
    print("post")
    print("traversalRecursion",s.traversalRecursion(root,"post"))
    print("traversalRecursion2",s.traversalRecursion2(root,"post"))
    print("traversalDFS",s.traversalDFS(root,"post"))
    print("traversalDFSpost",s.traversalDFSpost(root,"post"))
    print("traversalflagiter",s.traversalflagiter(root,"post"))
    print("level")
    print("traversalLevel",s.traversalLevel(root))
    print("traversalBFSlevel",s.traversalBFSlevel(root,None))
    print("traversalflagiter",s.traversalflagiter(root,"level"))

if __name__ == '__main__':
    main()
