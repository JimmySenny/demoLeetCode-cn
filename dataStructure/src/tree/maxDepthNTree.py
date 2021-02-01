#!/usr/bin/env python3

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children

class Solution:
    #def maxDepth(self, root: Node) -> int:
    def maxDepthNTreeRecursion(self, root):
        if not root:
            return 0
        elif None == root.children:
            return 1
        else:
            height = [self.maxDepthNTreeRecursion(c) for c in root.children ]
            return max(height) + 1
    def maxDepthNTreeLevel(self,root):
        res = 0
        if not root:
            return res
        cur = [root]
        while cur:
            lay, layval = [],[]
            for node in cur:
                layval.append(node.val)
                if node.children:
                    for i in range(len(node.children)):
                        lay.append(node.children[i])
            cur = lay
            res += 1
        return res;
    def maxDepthNTreeBFS(self,root):
        if not root:
            return 0
        res = 0
        qs = [root]
        while qs:
            size = len(qs)
            for i in range(size):
                cur = qs.pop(0)
                if cur.children:
                    for c in cur.children:
                        qs.append(c)
            res += 1
        return res
    def maxDepthNTreeDFS(self,root):
        stackTree= [root]
        stackDepth = [1]
        maxDepth = 0

        while stackTree:
            cur = stackTree.pop()
            curDepth = stackDepth.pop()
            if cur:
                maxDepth = max(curDepth, maxDepth)
                if cur.children:
                    for c in cur.children:
                        stackTree.append(c)
                        stackDepth.append(curDepth+1)
        return maxDepth

def main():
    n41 = Node(14)
    n33 = Node(13)
    n32 = Node(12)
    n31 = Node(11,[n41])
    n25 = Node(10)
    n24 = Node(9,[n33])
    n23 = Node(8,[n32])
    n22 = Node(7,[n31])
    n21 = Node(6)
    n14 = Node(5,[n24,n25])
    n13 = Node(4,[n23])
    n12 = Node(3,[n21,n22])
    n11 = Node(2)
    n01 = Node(1,[n11,n12,n13,n14])
    root = n01

    s = Solution()
    print(s.maxDepthNTreeRecursion(root))
    print(s.maxDepthNTreeLevel(root))
    print(s.maxDepthNTreeBFS(root))
    print(s.maxDepthNTreeDFS(root))

if __name__ == '__main__':
    main()
