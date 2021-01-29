#!/usr/bin/env  python3

import time

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BSTree:
    def __init__(self):
        self.root = None
        self.maxNum = float('-inf')
        self.minNum = float('inf')
    def findMaxNum(self):
        cur = self.root
        if not cur:
            return float('inf')
        while cur.right:
            cur = cur.right
        return cur.val if cur else float('-inf')
    def findMinNum(self):
        cur = self.root
        if not cur:
            return float('inf')
        while cur.left:
            cur = cur.left
        return cur.val if cur else float('inf')
    def insertIntoBSTRe(self, root, val):
        if not root:
            self.maxNum = val if val > self.maxNum else self.maxNum
            self.minNum = val if val < self.minNum else self.minNum
            return TreeNode(val)
        if root.val == val:
            return root
        elif root.val > val:
            root.left = self.insertIntoBSTRe(root.left, val)
        else:
            root.right = self.insertIntoBSTRe(root.right, val)
        return root
    def deleteNodeRe(self, root, val):
        node = self.recursiondeleteBST(root,val)
        if self.maxNum == val:
            self.maxNum = self.findMaxNum()
        if self.minNum == val:
            self.minNum = self.findMinNum()
        return node
    def recursiondeleteBST(self,root,val):
        if not root:
            return None
        if root.val > val:
            root.left = self.recursiondeleteBST(root.left, val)
        elif root.val < val:
            root.right = self.recursiondeleteBST(root.right, val)
        else: # root.val == val:
            # 叶子节点
            if not root.left and not root.right:
                root = None
            elif root.right:
                # 存在右子节点，则将右树中的最小的叶子节点赋值给当前节点并将其删除
                # 即右树中的最左叶子节点删除
                rightMin = root.right
                while rightMin.left:
                    rightMin = rightMin.left
                root.val = rightMin.val # 值交换
                #递归删除下一个节点
                root.right = self.recursiondeleteBST(root.right, root.val)
            else:
                leftMax = root.left
                while leftMax.right:
                    leftMax = leftMax.right
                root.val = leftMax.val
                root.left = self.recursiondeleteBST(root.left, root.val)

        return root # 必须返回root节点
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


    
class Solution:
    #def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        #考虑滑动窗口
        lens = len(nums)
        pl = 0 # 左指针
        pr = 1
        bst = BSTree()
        if lens > 0:
            bst.root = bst.insertIntoBSTRe(bst.root,nums[pl])
        #print("while0",pl,pr,lens)
        while pl < lens:
            if pl > 0:
                # 左移
                bst.deleteNodeRe(bst.root,nums[pl-1])
                pass
            #print("-while1",pl,pr,bst.maxNum,bst.minNum)
            while pr < lens and pr - pl <=k:
                if pl == pr:
                    pr += 1
                    break
                #print("--while2",pl,pr,nums[pr],bst.maxNum,bst.minNum)
                # nums [i] 和 nums [j] 的差的绝对值小于等于 t
                if abs(bst.minNum-nums[pr]) <= t or abs(bst.maxNum-nums[pr]) <= t:
                    return True
                bst.insertIntoBSTRe(bst.root,nums[pr])
                #print("==bstiter",bst.traversalflagiter(bst.root,"in"))
                #print("---while2",pl,pr,nums[pr],bst.maxNum,bst.minNum)
                pr += 1
            pl += 1
        return False

def main():
    s = Solution()
    nums1,k1,t1 = [1,2,3,1],3,0   #true
    nums2,k2,t2 = [1,0,1,1],1,2   #true
    nums3,k3,t3 = [1,5,9,1,5,9],2,3 #false
    nums4,k4,t4 = [1,2,5,6,7,2,4],4,0 #true
    nums5,k5,t5 = [1,2],0,1   #false
    nums6,k6,t6 = [1,2,1,1],1,0   #true
    nums7,k7,t7 = [4,1,6,3],100,1   #true

    timeStamp1 = time.time()
    print(s.containsNearbyAlmostDuplicate(nums1,k1,t1))
    print(s.containsNearbyAlmostDuplicate(nums2,k2,t2))
    print(s.containsNearbyAlmostDuplicate(nums3,k3,t3))
    print(s.containsNearbyAlmostDuplicate(nums4,k4,t4))
    print(s.containsNearbyAlmostDuplicate(nums5,k5,t5))
    print(s.containsNearbyAlmostDuplicate(nums6,k6,t6))
    print(s.containsNearbyAlmostDuplicate(nums7,k7,t7))
    timeStamp2 = time.time()
    """
    print(s.containsNearbyDuplicate1(nums,k))
    timeStamp3 = time.time()
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    """
    print(timeStamp3-timeStamp2)
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
