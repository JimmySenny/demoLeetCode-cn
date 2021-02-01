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

# Definition for a node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children= children

class Solution:
    # 对一个N叉树进行遍历
    #def traversalNTree(self, root: 'Node') -> List[int]:
    """递归 前后序"""
    def traversalNTreeRecursion(self, root, order="pre"):
        if not root:
            return []
        if "pre" == order:
            res = [root.val]
            if root.children:
                for node in root.children:
                    res.extend(self.traversalNTreeRecursion(node))
        elif "post" == order:
            res = []
            if root.children:
                for node in root.children:
                    res.extend(self.traversalNTreeRecursion(node))
            res.append(root.val)
        else:
            pass
        return res
    def traversalNTreeRecursion2(self, root, order="pre"):
        res = []
        self.recursionTraversalNTree(root,res,order)
        return res

    def recursionTraversalNTree(self, root,res,order):
        if not root:
            return
        count = len(root.children) if root.children else 0
        if "pre" == order:
            res.append(root.val)
            for i in range(count):
                self.recursionTraversalNTree(root.children[i],res,order)
        elif "post" == order:
            for i in range(count):
                self.recursionTraversalNTree(root.children[i],res,order)
            res.append(root.val)
        else:
            pass

        return None
    """DFS 前后序"""
    def traversalNTreeDFS(self,root,order="pre"):
        # 深度优先搜索
        """
        res = []
        stack = []
        cur = root
        #前序
        if "pre" == order:
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.children[0]
                cur = stack.pop()
                cur = cur.children[-1]
            return res
        #后序
        if "post" == order:
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.extend(cur.children)
                    cur = cur.children[-1]
                cur = stack.pop()
                cur = cur.children[0]
            return res[::-1]
        """
    def traversalNTreeDFSpre(self,root,order="pre"):
        # 深度优先
        if not root:
            return []
        res = []
        stack= [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.children:
                stack.extend(cur.children[::-1])
            """
                i = len(cur.children) - 1
                while i >= 0:
                    stack.append(cur.children[i])
                    i -= 1
            """
        return res
    def traversalNTreeDFSpost(self,root,order="post"):
        if not root:
            return []
        res = []
        stack= [root]
        while stack:
            cur = stack.pop()
            if cur.children:
                stack.extend(cur.children[:])
            """
                for i in range(len(cur.children)):
                    stack.append(cur.children[i])
            """
            res.append(cur.val)
        return res[::-1]
    """BFS 层序"""
    def traversalNTreeBFSlevel(self,root,order="level"):
        # 广度优先-层序遍历
        if not root:
            return []
        queue = [root]
        res = [root.val]
        while queue:
            cur = queue.pop(0)
            if cur.children:
                for i in range(len(cur.children)):
                    queue.append(cur.children[i])
                    res.append(cur.children[i].val)
        return res
    def traversalNTreeLevel(self,root):
        # 迭代-层序遍历
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            lay, layval = [],[]
            for node in cur:
                layval.append(node.val)
                if node.children:
                    for i in range(len(node.children)):
                        lay.append(node.children[i])
            cur = lay
            res.append(layval)
        return res
    def traversalNTreeFlagIter(self,root,order):
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
                    if cur.children:
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                    qs.append((1,cur))
                if "post" == order: # 左右根  re 根右左
                    qs.append((1,cur))
                    if cur.children:
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                if "level" == order:# 层序 先上再下先左后右 queue left right 
                    qs.append((1,cur))
                    if cur.children:
                        for i in range(len(cur.children)):
                            qs.append((0,cur.children[i]))
            else:
                res.append(cur.val)
        return res

    #@self.decorate_runTime_ms(self)
    def traversalSerializeUp2Down(self, root,order1="pre",order2="pre"):
        # 自顶向下递归
        # 两次遍历 重复遍历情况
        res = []
        self.recursionTraversalSerialize(root,res,order1,order2)
        return res
    def recursionTraversalSerialize(self, root,res,order1="pre",order2="pre"):
        # 按前序遍历每个节点
        if not root:
            return []
        #print("recursionTraversalSerializeDown2Up",root.val)
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
    def traversalSerializeDown2Up(self, root,order1="post",order2="post"):
        # 自底向上递归
        res = []
        res.append(self.recursionTraversalSerializeDown2Up(root,res,order1,order2))
        return res
    def recursionTraversalSerializeDown2Up(self,root,res,order1="post",order2="post"):
        if not root:
            return ''
        #print("recursionTraversalSerializeDown2Up",root.val)
        left = self.recursionTraversalSerializeDown2Up(root.left,res)
        right = self.recursionTraversalSerializeDown2Up(root.right,res)

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
    n22 = Node(6)
    n21 = Node(5)
    n13 = Node(4)
    n12 = Node(2)
    n11 = Node(3,[n21,n22])
    n01 = Node(1,[n11,n12,n13])

    root = n01

    s = Solution()
    print("N叉树的一次遍历")
    print("pre")
    print("traversalNTreeRecursion",s.traversalNTreeRecursion(root,"pre"))
    print("traversalNTreeRecursion2",s.traversalNTreeRecursion2(root,"pre"))
    print("traversalNTreeDFS",s.traversalNTreeDFS(root,"pre"))
    print("traversalNTreeDFSpre",s.traversalNTreeDFSpre(root,"pre"))
    print("traversalNTreeFlagIter",s.traversalNTreeFlagIter(root,"pre"))

    print("post")
    print("traversalNTreeRecursion",s.traversalNTreeRecursion(root,"post"))
    print("traversalNTreeRecursion2",s.traversalNTreeRecursion2(root,"post"))
    print("traversalNTreeDFS",s.traversalNTreeDFS(root,"post"))
    print("traversalNTreeDFSpost",s.traversalNTreeDFSpost(root,"post"))
    print("traversalNTreeFlagIter",s.traversalNTreeFlagIter(root,"post"))

    print("level")
    print("traversalNTreeBFSlevel",s.traversalNTreeBFSlevel(root,"post"))
    print("traversalNTreeLevel",s.traversalNTreeLevel(root))
    print("traversalNTreeFlagIter",s.traversalNTreeFlagIter(root,"level"))


    """
    print("树的每一个节点的序列")
    timeStamp1 = time.time()
    print("traversalSerializeUp2Down",s.traversalSerializeUp2Down(root,"pre","pre"))
    timeStamp2 = time.time()
    print("traversalSerializeDown2Up",s.traversalSerializeDown2Up(root,"post","post"))
    timeStamp3 = time.time()
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)
    """

if __name__ == '__main__':
    main()
