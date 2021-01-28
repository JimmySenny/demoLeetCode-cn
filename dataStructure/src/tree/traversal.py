#!/usr/bin/env python3

import time
from functools import wraps

"""
def decorate_runTime_ms(func):
    @wrap(func)
    def wrap(*args,**kwargs):
        import time
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('%s() runTime:%s ms'%(func.__name__,int(1000*(end_time-start_time))))
        return func
        #return f
    return wrap
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #def traversal(self, root: TreeNode) -> List[int]:
    # 对一个树进行遍历的不同方法模板
    def traversalRecursion(self, root,order="pre"):
        # 递归-整体
        if not root:
            return []
        #print("traversalRecursion",root.val)
        if "pre" == order:
            return [root.val] + self.traversalRecursion(root.left,order) + self.traversalRecursion(root.right,order)
        elif "in" == order:
            return self.traversalRecursion(root.left,order) + [root.val] + self.traversalRecursion(root.right,order)
        elif "post" == order:
            return self.traversalRecursion(root.left,order) + self.traversalRecursion(root.right,order) + [root.val]
        else:
            return None
    def traversalRecursion2(self, root,order="pre"):
        # 递归-逐个节点
        res = []
        self.recursionTraversal(root,res,order)
        return res
    def recursionTraversal(self,curr,res,order):
        if not curr:
            return []
        if "pre" == order: 
            res.append(curr.val)
            self.recursionTraversal(curr.left,res,order)
            self.recursionTraversal(curr.right,res,order)
        elif "in" == order:
            self.recursionTraversal(curr.left,res,order)
            res.append(curr.val)
            self.recursionTraversal(curr.right,res,order)
        elif "post" == order:
            self.recursionTraversal(curr.left,res,order)
            self.recursionTraversal(curr.right,res,order)
            res.append(curr.val)
        else:
            return None
    def traversalRecursion3(self, root,order="pre"):
        # 同recursion2 
        return self.recursion3(root,order)
    def recursion3(self,root,order):
        if not root:
            return None
        if "pre" == order:
            print(root.val,end='|')
            nodeleft = self.recursion3(root.left,order)
            noderight = self.recursion3(root.right,order)
        elif "in" == order:
            nodeleft = self.recursion3(root.left,order)
            print(root.val,end='|')
            noderight = self.recursion3(root.right,order)
        elif "post" == order:
            nodeleft = self.recursion3(root.left,order)
            noderight = self.recursion3(root.right,order)
            print(root.val,end='|')
        else: #"other" == order:
            print(root.val,end='|')
            noderight = self.recursion3(root.right,order)
            nodeleft = self.recursion3(root.left,order)
        return 
    def traversalDFS(self,root,order="pre"):
        # 深度优先搜索
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
        # 深度优先 另一种形式
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
    def traversalBFSlevel(self,root,order="pre"):
        # 广度优先-层序遍历
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
        # 迭代-层序遍历
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
        return res

    #@self.decorate_runTime_ms(self)
    def traversalSerialize(self, root,order1="pre",order2="pre"):
        # 两次遍历 重复遍历情况
        res = []
        self.recursionTraversalSerialize(root,res,order1,order2)
        return res
    def recursionTraversalSerialize(self, root,res,order1="pre",order2="pre"):
        # 按前序遍历每个节点
        if not root:
            return []
        #print("recursionTraversalSerializeOne",root.val)
        # 遍历到的当前节点
        if "pre" == order1:
            chain = self.traversalRecursion(root,order2)
            res.append(chain)
            #print(root.val,"--",str(chain))
            left = self.recursionTraversalSerialize(root.left,res,order1,order2)
            right = self.recursionTraversalSerialize(root.right,res,order1,order2)
        elif "in" == order1:
            left = self.recursionTraversalSerialize(root.left,res,order1,order2)
            chain = self.traversalRecursion(root,order2)
            res.append(chain)
            #print(root.val,"--",str(chain))
            right = self.recursionTraversalSerialize(root.right,res,order1,order2)
        elif "post" == order1:
            left = self.recursionTraversalSerialize(root.left,res,order1,order2)
            right = self.recursionTraversalSerialize(root.right,res,order1,order2)
            chain = self.traversalRecursion(root,order2)
            res.append(chain)
            #print(root.val,"--",str(chain))
        return chain
    #@decorate_runTime_ms()
    def traversalSerializeOne(self, root,order1="post",order2="post"):
        res = []
        res.append(self.recursionTraversalSerializeOne(root,res,order1,order2))
        return res
    def recursionTraversalSerializeOne(self,root,res,order1="post",order2="post"):
        if not root:
            return ''
        #print("recursionTraversalSerializeOne",root.val)
        left = self.recursionTraversalSerializeOne(root.left,res)
        right = self.recursionTraversalSerializeOne(root.right,res)

        chain = left + ',' + right + ',' + str(root.val)
        res.append(chain)
        #print(root.val,"--",str(chain))

        return chain
    def decorate_runTime_ms(func):
        #@wrap(func)
        def wrap(self,*args,**kwargs):
            import time
            start_time = time.time()
            f = func(*args,**kwargs)
            end_time = time.time()
            print('%s() runTime:%s ms'%(func.__name__,int(1000*(end_time-start_time))))
            return f
        return wrap
    



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
    print("树的一次遍历")
    print("pre")
    print("traversalRecursion",s.traversalRecursion(root,"pre"))
    print("traversalRecursion2",s.traversalRecursion2(root,"pre"))
    print("traversalRecursion3")
    s.traversalRecursion3(root,"pre")
    print()
    print("traversalDFS",s.traversalDFS(root,"pre"))
    print("traversalDFSpre",s.traversalDFSpre(root,"pre"))
    print("traversalflagiter",s.traversalflagiter(root,"pre"))
    print("in")
    print("traversalRecursion",s.traversalRecursion(root,"in"))
    print("traversalRecursion2",s.traversalRecursion2(root,"in"))
    print("traversalRecursion3")
    s.traversalRecursion3(root,"in")
    print()
    print("traversalDFS",s.traversalDFS(root,"in"))
    print("traversalflagiter",s.traversalflagiter(root,"in"))
    print("post")
    print("traversalRecursion",s.traversalRecursion(root,"post"))
    print("traversalRecursion2",s.traversalRecursion2(root,"post"))
    print("traversalRecursion3")
    s.traversalRecursion3(root,"post")
    print()
    print("traversalDFS",s.traversalDFS(root,"post"))
    print("traversalDFSpost",s.traversalDFSpost(root,"post"))
    print("traversalflagiter",s.traversalflagiter(root,"post"))
    print("level")
    print("traversalBFSlevel",s.traversalBFSlevel(root,None))
    print("traversalLevel",s.traversalLevel(root))
    print("traversalflagiter",s.traversalflagiter(root,"level"))

    print("traversalRecursion3-other")
    s.traversalRecursion3(root,"other")
    print()

    print("树的每一个节点的序列")
    timeStamp1 = time.time()
    print("traversalSerialize",s.traversalSerialize(root,"pre","pre"))
    timeStamp2 = time.time()
    print("traversalSerializeOne",s.traversalSerializeOne(root,"post","post"))
    timeStamp3 = time.time()
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)

if __name__ == '__main__':
    main()
