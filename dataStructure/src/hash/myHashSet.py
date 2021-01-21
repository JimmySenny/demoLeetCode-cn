#!/usr/bin/env python3

class MyHashSet:
    def __init__(self):
        #Initialize your data structure here.
        # 桶大小
        self.keyRange = 3  # 质数，可以减少潜在的碰撞
        # 使用链表
        #self.bucketArray = [ BucketLinkList() for i in range(self.keyRange) ]
        # 使用二叉树
        self.bucketArray = [ BucketBTree() for i in range(self.keyRange) ]
        
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
            print("i,self.bucketArray[i]:",i,self.bucketArray[i].iterKey())

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
链表实现
"""
class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
class BucketLinkList:
    def __init__(self):
        self.head = ListNode(0)
    def insert(self, newvalue):
        if not self.exists(newvalue):
            # 新节点 插入head后 
            newNode = ListNode(newvalue,self.head.next)
            self.head.next = newNode
    def delete(self,value):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.value == value:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
    def exists(self, value):
        cur = self.head.next
        while cur:
            if value == cur.value:
                return True
            cur = cur.next
        return False
    def iterKey(self):
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
"""
二叉树实现
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class BTree:
    def __init__(self):
        self.root = None
    def searchBTree(self, root,value):
        if not root:
            return False
        print("---search:",root.value,value)
        if value == root.value:
            return True
        if value > root.value:
            self.searchBTree(root.right,value)
        else:
            self.searchBTree(root.left,value)
    def insertBTree(self, root, value):
        if not root:
            return TreeNode(value)
        if value == root.value:
            return root
        elif value > root.value:
            root.right = self.insertBTree(root.right, value)
        else:
            root.left = self.insertBTree(root.left, value)
        return root
    def deleteBTree(self, root, value):
        if not root:
            return None
        #delete the current node
        print("value,root.value", value, root.value)
        if value == root.value:
            # the node is a leaf 叶子节点
            if not root.left and not root.right:
                root = None 
            #存在右子节点，则将右树中的最小的叶子节点赋值给当前节点，并将其删除
            #即右树中的最左叶子节点
            elif root.right:
                rightMin = root.right
                while rightMin.left:
                    rightMin = rightMin.left
                root.value = rightMin.value
                # 可能是一个没有左叶的根节点
                root.right = self.deleteBTree(root.right, root.value)
            else: # root.left
                #同理 将左子树最大的
                leftMax = root.left
                while leftMax.right:
                    leftMax = leftMax.right
                root.value = leftMax.value
                root.left = self.deleteBTree(root.left, root.value)
            pass
        elif value > root.value:
            root.right = self.deleteBTree(root.right, value)
        else:
            root.left = self.deleteBTree(root.left, value)
            pass
        return root
    def iterBTree(self, root, order = 'pre'):
        res = []
        self.recursionIterBTree(root,res,order)
        return res
    def recursionIterBTree(self, root, res, order):
        if not root:
            return []
        if "pre" == order:
            res.append(root.value)
            self.recursionIterBTree(root.left, res, order)
            self.recursionIterBTree(root.right, res, order)
        if "in" == order:
            self.recursionIterBTree(root.left, res, order)
            res.append(root.value)
            self.recursionIterBTree(root.right, res, order)
        if "post" == order:
            self.recursionIterBTree(root.left, res, order)
            self.recursionIterBTree(root.right, res, order)
            res.append(root.value)
class BucketBTree:
    def __init__(self):
        self.tree = BTree()
    def insert(self, value):
        self.tree.root = self.tree.insertBTree(self.tree.root, value)
    def delete(self, value):
        print("delete:",value)
        #print("searchResult:",self.exists(value))
        """
        if not self.exists(value):
            return None
        """
        self.tree.root = self.tree.deleteBTree(self.tree.root, value)
    def exists(self, value):
        print("exists:", self.tree.root.value, value)
        return self.tree.searchBTree(self.tree.root, value)
    def iterKey(self):
        res = []
        res.append( self.tree.iterBTree(self.tree.root,"pre") )
        res.append( self.tree.iterBTree(self.tree.root, "in") )
        res.append( self.tree.iterBTree(self.tree.root, "post") )
        return res


def main():
    hash = MyHashSet()
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

if __name__ == '__main__':
    main()
