#!/usr/bin/env  python3

import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    def findDuplicateSubtrees(self, root):
        # 二叉树序列化，递归序列化节点，进行判断
        # 每个序列化及其对应的根节点作为map保存，若k重复，则v加入返回的list
        # 前序遍历序列化
        hashMap = {}
        res = []
        self.serializePre(root,hashMap,res)
        return res
    def findDuplicateSubtrees1(self, root):
        # 优化 后序遍历序列化(前序遍历时存在重复遍历)
        hashMap = {}
        res = []
        self.serializePost(root,hashMap,res)
        return res
    def serializePre(self,root,hashMap,res):
        if not root:
            return []
        chain = self.recursionSerializePre(root)
        print(root.val,":",str(chain))
        if hashMap.__contains__(str(chain)):
            hashMap[str(chain)] += 1
            # 可能有多个 为使结果不重复，当v为2则给res即可，大于2不用管
            if 2 == hashMap[str(chain)]:
                res.append(root.val)
        else:
            hashMap[str(chain)] = 1
        left = self.serializePre(root.left,hashMap,res)
        right = self.serializePre(root.right,hashMap,res)
        return res
    def recursionSerializePre(self,root):
        if not root:
            return "#"
        return str(root.val)+','+self.recursionSerializePre(root.left)+','+self.recursionSerializePre(root.right)
    def serializePost(self,root,hashMap,res):
        if not root:
            return '#'
        left = self.serializePost(root.left,hashMap,res)
        right = self.serializePost(root.right,hashMap,res)

        chain = left+','+right+','+str(root.val)
        print(root.val,":",str(chain))
        if hashMap.__contains__(str(chain)):
            hashMap[str(chain)] += 1
            # 可能有多个 为使结果不重复，当v为2则给res即可，大于2不用管
            if 2 == hashMap[str(chain)]:
                res.append(root.val)
        else:
            hashMap[str(chain)] = 1
        return chain

def main():
    n34 = TreeNode(5)
    n33 = TreeNode(4)
    n32 = TreeNode(5)
    n31 = TreeNode(4)
    n24 = TreeNode(3)
    n23 = TreeNode(2,n33,n34)
    n22 = TreeNode(3)
    n21 = TreeNode(2,n31,n32)
    n12 = TreeNode(1,n23,n24)
    n11 = TreeNode(1,n21,n22)
    n00 = TreeNode(0,n11,n12)
    root = n00

    s = Solution()
    timeStamp1 = time.time()
    print(s.findDuplicateSubtrees(root))
    timeStamp2 = time.time()
    print(s.findDuplicateSubtrees1(root))
    timeStamp3 = time.time()
    """
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)
    """
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
