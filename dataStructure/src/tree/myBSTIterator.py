#!/usr/bin/env python3

from traversal import Solution as TreeTraversal
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

class BSTIterator:
    #def __init__(self, root: TreeNode):
    def __init__(self, root):
        tr = TreeTraversal()
        self.index = 0
        self.iter = tr.traversalflagiter(root,"in")

    #def next(self) -> int:
    def next(self):
        if self.hasNext():
            self.index += 1
            return self.iter[self.index]
        return -1

    #def hasNext(self) -> bool:
    def hasNext(self):
        if self.index < len(self.iter) -1:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def main():
    n22 = TreeNode(20)
    n21 = TreeNode(9)
    n12 = TreeNode(15,n21,n22)
    n11 = TreeNode(3)
    n1 = TreeNode(7,n11,n12)

    root = n1

    s = TreeTraversal()
    print("in")
    print("traversalRecursion",s.traversalRecursion(root,"in"))
    print("traversalRecursion2",s.traversalRecursion2(root,"in"))
    print("traversalRecursion3")
    s.traversalRecursion3(root,"in")
    print()
    print("traversalDFS",s.traversalDFS(root,"in"))
    print("traversalflagiter",s.traversalflagiter(root,"in"))

    obj = BSTIterator(root)
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())

    """
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
    """

if __name__ == '__main__':
    main()
