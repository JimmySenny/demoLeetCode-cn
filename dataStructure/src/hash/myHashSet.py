#!/usr/bin/env python3

class MyHashSet:
    def __init__(self):
        #Initialize your data structure here.
        # 桶大小
        self.keyRange = 2  # 质数，可以减少潜在的碰撞
        # 使用链表
        #self.bucketArray = [ BucketLinkList() for i in range(self.keyRange) ]
        # 使用二叉树
        self.bucketArray = [ BucketBSTree() for i in range(self.keyRange) ]
        
#    def _hash(self, key)->int:
    def _hash(self, key):
        return key % self.keyRange
#    def add(self, key: int) -> None:
    def add(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)
#    def remove(self, key: int) -> None:
    def remove(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
#    def contains(self, key: int) -> bool:
    def contains(self, key):
        #Returns true if this set contains the specified element
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
    def hashIter(self):
        for i in range(self.keyRange):
            print("i,self.bucketArray[i]:",i,self.bucketArray[i])
            print(self.bucketArray[i].iterKey())

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
链表实现
"""
class ListNode:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next
class BucketLinkList:
    def __init__(self):
        self.head = ListNode(0)
    def insert(self, newkey):
        if not self.exists(newkey):
            # 新节点 插入head后 
            newNode = ListNode(newkey,self.head.next)
            self.head.next = newNode
    def delete(self,key):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
    def exists(self, key):
        cur = self.head.next
        while cur:
            if key == cur.key:
                return True
            cur = cur.next
        return False
    def iterKey(self):
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.key)
            cur = cur.next
        return res
"""
二叉排序树实现
"""
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
class BSTree:
    def __init__(self):
        self.root = None
    def searchBSTree(self, root,key):
        if not root:
            return False
        if key == root.key:
            return True
        if key > root.key:
            return self.searchBSTree(root.right,key)
        else:
            return self.searchBSTree(root.left,key)
    def insertBSTree(self, root, key):
        print("insertkey",key,root)
        if not root:
            return TreeNode(key)
        if key == root.key:
            return root
        elif key > root.key:
            root.right = self.insertBSTree(root.right, key)
        else:
            root.left = self.insertBSTree(root.left, key)
        return root
    def deleteBSTree(self, root, key):
        if not root:
            return None
        #delete the current node
        print("key,root.key", key, root.key)
        if key > root.key:
            root.right = self.deleteBSTree(root.right, key)
        elif key < root.key:
            root.left = self.deleteBSTree(root.left, key)
        else: # key == root.key:
            # the node is a leaf 叶子节点
            if not root.left and not root.right:
                root = None 
            #存在右子节点，则将右树中的最小的叶子节点赋值给当前节点，并将其删除
            #即右树中的最左叶子节点
            elif root.right:
                rightMin = root.right
                while rightMin.left:
                    rightMin = rightMin.left
                root.key = rightMin.key
                # 可能是一个没有左叶的根节点
                root.right = self.deleteBSTree(root.right, root.key)
            else: # root.left
                #同理 将左子树最大的
                leftMax = root.left
                while leftMax.right:
                    leftMax = leftMax.right
                root.key = leftMax.key
                root.left = self.deleteBSTree(root.left, root.key)
        return root
    def iterBSTree(self, root, order = 'pre'):
        res = []
        self.recursionIterBSTree(root,res,order)
        return res
    def recursionIterBSTree(self, root, res, order):
        if not root:
            return []
        if "pre" == order:
            res.append(root.key)
            self.recursionIterBSTree(root.left, res, order)
            self.recursionIterBSTree(root.right, res, order)
        if "in" == order:
            self.recursionIterBSTree(root.left, res, order)
            res.append(root.key)
            self.recursionIterBSTree(root.right, res, order)
        if "post" == order:
            self.recursionIterBSTree(root.left, res, order)
            self.recursionIterBSTree(root.right, res, order)
            res.append(root.key)
class BucketBSTree:
    def __init__(self):
        self.tree = BSTree()
    def insert(self, key):
        self.tree.root = self.tree.insertBSTree(self.tree.root, key)
        print("i",self.tree.root)
    def delete(self, key):
        print("delete:",key)
        print("searchResult:",self.exists(key))
        if not self.exists(key):
            return None
        self.tree.root = self.tree.deleteBSTree(self.tree.root, key)
    def exists(self, key):
        return self.tree.searchBSTree(self.tree.root, key)
    def iterKey(self):
        res = []
        res.append( self.tree.iterBSTree(self.tree.root,"pre") )
        res.append( self.tree.iterBSTree(self.tree.root, "in") )
        res.append( self.tree.iterBSTree(self.tree.root, "post") )
        return res

"""
位实现
由范围可知最大 1000000
而一个无符号整数有32bit，可表示32个数(s32位操作系统)
故可理解为1000000/32个桶
判断key的值 是否存在就去 桶为 k/32 的 k%32 位。 
k/32 等价于 k>>5(左移） k%32 等价于 k&31.（逻辑与))
"""
class BucketBit:
    def __init__(self):
        self.intlen = 65536
        self.bitand = 65535
        self.bitmov = 16
        self.hashset = [0 for i in range(10000000//self.intlen)]

    def add(self, key):
        self.hashset[key>>self.bitmov] |= 1<<(key&self.bitand)

    def remove(self, key):
        self.hashset[key>>self.bitmov] &= ~(1<<(key&self.bitand))

    def contains(self, key):
        return self.hashset[key>>self.bitmov] & 1<<(key&self.bitand) != 0



def main():
    hash = MyHashSet()
    """
    hash.add(0)
    hash.add(10)
    hash.add(2)
    hash.add(0)
    hash.add(3)
    hash.add(1)
    hash.add(4)
    hash.add(13)
    hash.add(7)
    hash.add(19)
    hash.add(16)
    hash.hashIter()
    print("contains:",hash.contains(0))
    print("contains:",hash.contains(3))
    print("contains:",hash.contains(5))
    print("contains:",hash.contains(6))
    print("contains:",hash.contains(10))
    print("contains:",hash.contains(13))
    hash.remove(2)
    hash.remove(5)
    hash.remove(13)
    hash.hashIter()
    hash.remove(10)
    hash.hashIter()
    """
    hash.add(10)
    hash.add(11)

    hash.add(6)
    hash.add(7)
    hash.hashIter()

if __name__ == '__main__':
    main()
