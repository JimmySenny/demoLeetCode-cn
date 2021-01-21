#!/usr/bin/env python3

from traversal import Solution as tr

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serializeRe(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        return self.recursionSerialize(root,res)
    def recursionSerialize(self,root,res):
        # 递归(前序遍历)实现
        if not root:
            res += str(None) 
            res += ","
        else:
            res += str(root.val) + ","
            res = self.recursionSerialize(root.left, res)
            res = self.recursionSerialize(root.right, res)
        return res
    def deserializeRe(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        print(type(data))
        array = data.split(",")
        datalist = list(array)
        return self.recursionDeserialize(datalist)
    def recursionDeserialize(self,datalist):
        # 递归 逐个弹出 list 的首项（根节点值），构建当前子树的根节点，
        # 顺着list，就会先构建根节点 > 构建左子树 > 构建右子树
        dlen = len(datalist)
        if 0 == dlen:
            return None
        if 'None' == datalist[0] or '' == datalist[0]:
            datalist.pop(0)
            return None
        print(datalist)
        root = TreeNode(int(datalist[0]))
        datalist.pop(0)
        root.left = self.recursionDeserialize(datalist)
        root.right = self.recursionDeserialize(datalist)
        return root

    def serializeBFS(self,root):
        queue = [root]
        res = ""
        while queue:
            cur = queue.pop(0)
            if cur:
                res += str(cur.val) + ","
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res += str(None)
                res += ","
        return res
    def deserializeBFS(self, data):
        datalist = list(data.split(","))
        print(datalist)
        if 'None' == datalist[0] or '' == datalist[0]:
            return None
        root = TreeNode(int(datalist[0]))
        queue = [root]
        index = 1 
        # 最后有一个逗号，造成''，故条件-1
        while index < len(datalist) - 1:
            cur = queue.pop(0)
            valLeft = datalist[index]
            valRight = datalist[index+1]
            print("i,vl,vr",index,valLeft,valRight)
            if 'None' != valLeft: # 真实节点
                nodeLeft = TreeNode(int(valLeft)) #父节点挂接
                cur.left = nodeLeft
                queue.append(nodeLeft)
            if 'None' != valRight:
                nodeRight = TreeNode(int(valRight))
                cur.right = nodeRight
                queue.append(nodeRight)
            # 一次考察一对子节点，指针加2
            index += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

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
    s = tr()
    print(s.traversalflagiter(root,"pre"))

    c = Codec()
    print("serializeRe")
    res = c.serializeRe(root)
    print(res)
    rootRe = c.deserializeRe(res)
    print(s.traversalflagiter(rootRe,"pre"))
    
    print(s.traversalflagiter(root,"level"))
    print("serializeBFS")
    res = c.serializeBFS(root)
    print(res)
    rootBFS = c.deserializeBFS(res)
    print(s.traversalflagiter(rootBFS,"level"))

if __name__ == '__main__':
    main()
