#!/usr/bin/env python3

class MyHashMap:
    def __init__(self):
        #Initialize your data structure here.
        # 桶大小
        self.keyRange = 2  # 质数，可以减少潜在的碰撞
        # 使用链表
        #self.bucketArray = [ BucketLinkList() for i in range(self.keyRange) ]
        # 使用二叉树
        self.bucketArray = [ BucketBSTree() for i in range(self.keyRange) ]
        
    #def _hash(self, key)->int:
    def _hash(self, key):
        return key % self.keyRange
    #def get(self, key: int) -> int:
    def get(self, key):
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].select(key)
    #def put(self, key: int, value: int) -> None:
    def put(self, key,value):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].update(key,value)
    def remove(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
    #def contains(self, key: int) -> bool:
    def contains(self, key):
        #Returns true if this set contains the specified element
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
    def hashIter(self):
        for i in range(self.keyRange):
            #print("i,self.bucketArray[i]:",i,self.bucketArray[i].tree.root)
            print(i,self.bucketArray[i].iterKV())


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
"""
链表实现
"""
class ListNode:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value 
        self.next = next
class BucketLinkList:
    def __init__(self):
        self.head = ListNode(0,None)
    def select(self,key):
        cur = self.head.next
        while cur:
            if key == cur.key:
                return cur.value
            cur = cur.next
        return -1
    def update(self, newkey, newvalue):
        # 新节点 插入head后 
        cur = self.head.next
        while cur:
            if newkey == cur.key:
                cur.value = newvalue
                return None
            cur = cur.next
        # 新节点 插入head后 
        newNode = ListNode(newkey,newvalue,self.head.next)
        self.head.next = newNode
        return None

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
    def iterKV(self):
        cur = self.head.next
        res = []
        while cur:
            res.append(str(cur.key)+"|"+str(cur.value))
            cur = cur.next
        return res
"""
二叉排序树实现 
TODO 测试集未过 待确认
"""
class TreeNode:
    def __init__(self, key=None,value=-1,left=None, right=None):
        self.key = key
        self.value = value
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
    def selectBSTree(self, root,key):
        if not root:
            return -1
        if key == root.key:
            return root.value
        if key > root.key:
            return self.selectBSTree(root.right,key)
        else:
            return self.selectBSTree(root.left,key)
    def updateBSTree(self, root, key,value):
        if not root:
            return TreeNode(key,value)
        pre = root
        cur = root
        print("root,cur1",key,root,cur,pre)
        # 如果有 则更新
        while cur:
            if key == cur.key:
                cur.value = value
                print("root,cur2",root,cur,pre)
                return root # root必须返回
            pre = cur
            if key > cur.key:
                cur = cur.left
            else:
                cur = cur.right

        if key > pre.key:
            pre.left = TreeNode(key,value)
        else:
            pre.right = TreeNode(key,value)

        print("root,cur3",root,cur,pre)
        return root
    def deleteBSTree(self, root, key):
        if not root:
            return None
        #delete the current node
        print("key,root.key", key, root.key)
        if key == root.key:
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
        elif key > root.key:
            root.right = self.deleteBSTree(root.right, key)
        else:
            root.left = self.deleteBSTree(root.left, key)
        return root
    def iterBSTree(self, root, order = 'pre'):
        res = []
        self.recursionIterBSTree(root,res,order)
        return res
    def recursionIterBSTree(self, root, res, order):
        if not root:
            return []
        if "pre" == order:
            #res.append(str(root.root)+"|"+str(root.value))
            res.append(root.value)
            self.recursionIterBSTree(root.left, res, order)
            self.recursionIterBSTree(root.right, res, order)
        if "in" == order:
            self.recursionIterBSTree(root.left, res, order)
            #res.append(str(root.root)+"|"+str(root.value))
            res.append(root.value)
            self.recursionIterBSTree(root.right, res, order)
        if "post" == order:
            self.recursionIterBSTree(root.left, res, order)
            self.recursionIterBSTree(root.right, res, order)
            #res.append(str(root.root)+"|"+str(root.value))
            res.append(root.value)
class BucketBSTree:
    def __init__(self):
        self.tree = BSTree()
    def select(self, key):
        return self.tree.selectBSTree(self.tree.root, key)
    def update(self, key,value):
        self.tree.root = self.tree.updateBSTree(self.tree.root,key,value)
    def delete(self, key):
        if not self.exists(key):
            return None
        self.tree.root = self.tree.deleteBSTree(self.tree.root, key)
    def exists(self, key):
        return self.tree.searchBSTree(self.tree.root, key)
    def iterKV(self):
        res = []
        res.append( self.tree.iterBSTree(self.tree.root,"pre") )
        res.append( self.tree.iterBSTree(self.tree.root, "in") )
        res.append( self.tree.iterBSTree(self.tree.root, "post") )
        return res

def main():
    hash = MyHashMap()
    """
    hash.put(10,10)
    hash.put(7,7)
    hash.put(2,2)
    hash.put(0,0)
    hash.put(3,3)
    hash.put(1,1)
    hash.put(0,0)
    hash.put(4,4)
    hash.put(13,13)
    hash.put(19,19)
    hash.put(16,16)
    hash.hashIter()
    hash.put(10,100)
    hash.put(10,10)
    hash.put(11,11)
    hash.put(2,2)
    hash.put(3,3)
    hash.hashIter()
    print("get:0",hash.get(0))
    print("get:2",hash.get(2))
    print("get:13",hash.get(13))
    print("get:5",hash.get(5))
    hash.remove(2)
    hash.remove(5)
    hash.remove(13)
    hash.hashIter()
    hash.remove(10)
    hash.hashIter()
    """

    hash.put(10,10)
    hash.put(11,11)
    hash.put(6,6)
    hash.put(15,15)
    hash.put(3,3)
    hash.put(8,8)
    hash.hashIter()
    hash.put(6,7)
    hash.hashIter()

if __name__ == '__main__':
    main()
