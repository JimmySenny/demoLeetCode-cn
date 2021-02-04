#!/usr/bin/env python3

import collections
import time

from myTrie import Trie

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)
        self.idx = -1 

class Solution:
    """
    xor 涉及位运算，需要每个数字的二进制值，在此基础上求异或值
    先将整数转化成二进制形式，再从最左侧的比特位开始逐一处理来构建最大异或值。
    #def findMaximumXOR(self, nums: List[int]) -> int:
    """
    """
    利用字典树存储按位前缀
    1 将每个数字按位存入前缀树，位数一致前补0 
    2.1 基于贪心，求得最高位不一致的位置
    2.2 在前缀树中不一致位置开始通过贪心求得每个数字的位数最大可能性异或值
    3 求得最大的异或值
    """
    def findMaximumXOR(self, nums):
        # 贪心 找到最高位1 即可保证xor最大
        """
        self.insertTrie(nums)
        head = self.findHeadForce(self.root)
        self.searchMaxXOR(head,nums)
        """
        return self.searchMaxXOR(self.findHeadDFS(self.insertTrie(nums)),nums)
    """
    利用哈希集合存储按位前缀
    """
    def findMaximumXORHash(self, nums):
        # bin(dec): 0bXXX
        #print(max(nums),bin(max(nums)),L)
        L = len(bin(max(nums))) - 2
        maxXor = 0
        for idx in range(L)[::-1]:
            # 将 max_xor 左移，释放出下一比特位的位置
            maxXor <<= 1
            # 将 max_xor 最右侧的比特置为 1
            curXor = maxXor | 1
            # 将长度为 L - iL−i 的按位前缀加入哈希集合 prefixes
            prefixes = {num >> idx for num in nums}
            # 遍历所有可能的按位前缀，检查是否存在 p1，p2 使得 p1^p2 == curr_xor
            maxXor |= any(curXor^p in prefixes for p in prefixes)
        return maxXor

    def __init__(self):
        self.root = TrieNode()
        self.dicl = ['0','1']
    def insertTrie(self, nums):
        #按位字典树:
        for num in nums:
            node = self.root
            print("insert num:", num,node,list(node.children))
            """
            for bit in '{:032b}'.format(num):
                node = node.children[bit]
                #print( bit, node)
            #print(node)
            """
            for idx in range(7,-1,-1):
                pre = node
                node.idx = idx
                val = num >> idx & 1
                node = node.children[str(val)]
                print(idx,val,pre.idx,pre,list(pre.children),pre.children[str(val)],node)
            node.isEnd = True
            print(pre.isEnd,node.isEnd,pre,node,list(node.children))
        return self.root
    def findHeadDFS(self, root):
        if not root:
            return self.root
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.children:
                count = len(cur.children)
                if 2 > count:
                    for s in self.dicl:
                        print("s:",s,list(cur.children),cur,cur.children[s])
                        if s in cur.children:
                            pre = cur
                            stack.append(cur.children[s])
                else:
                    print("break",pre,pre.idx,cur,cur.idx,list(cur.children))
                    break
        #return pre 
        return cur
    """
    def findHeadForce(self, root):
        if not root:
            return self.root
        node = root
        while node.children:
            if len(list(node.children)) > 1:
                break
            # 有可能 001100 和 001011 第三位还是一致的
            node = node.children['0']
        print("return:",node.idx,node,list(node.children))
        return node
    """
    def searchMaxXOR(self, head, nums):
        maxXor = 0
        for num in nums:
            maxXor = max(maxXor, self.searchXorNum(head,num))
        return maxXor

    def searchXorNum(self, head, num):
        cur = head
        print("head:",head,list(head.children))
        xorNum = 0
        #xorNum <<= 1
        #xorNum = (xorNum << 1) | 1
        print(num)
        while cur.children:
            val = (num>>cur.idx) & 1
            tmp = 'x'
            #print(cur.idx,cur.isEnd,val,list(cur.children),cur.children)
            print(cur.idx,cur.isEnd,val,list(cur.children),end='|')
            # 剪枝计算bit位 贪心求得最大值
            # 如果当前比特值存在互补比特值，访问具有互补比特值的孩子节点 该位结果为1
            # 如果不存在，直接访问具有当前比特值的孩子节点 该为结果为0
            if 0 == val:
                if '1' in cur.children:
                    # 也可以通过 cur.idx 进行计算累加
                    cur = cur.children['1']
                    xorNum = (xorNum << 1) | 1
                    tmp = 'a'
                else:
                    cur = cur.children['0']
                    xorNum <<= 1
                    tmp = 'b'
            else:
                if '0' in cur.children:
                    cur = cur.children['0']
                    xorNum = (xorNum << 1) | 1
                    tmp = 'c'
                else:
                    cur = cur.children['1']
                    xorNum <<= 1
                    tmp = 'd'
            print(cur.idx,cur.isEnd,tmp,xorNum)
            #xorNum = max(xorNum, num ^ cur.idx )
        return xorNum
    def traversal(self):
        t = Trie()
        t.root = self.root
        diclist = ['1','0']
        print(t.traversalTrieLevel(t.root, diclist))
        print(t.traversalTrieFlagIter(t.root, diclist,"level"))
        #print(t.traversalTrieDFS(t.root, diclist))

    """
    利用哈希集合存储按位前缀
    """

def main():
    s = Solution()
    nums1 = [3, 10, 5, 25, 2, 8]
    #nums1 = [2,3,5,8,10,25]
    #nums1 = [4,6,7]
    timeStamp1 = time.time()
    print("result:",s.findMaximumXOR(nums1))
    timeStamp2 = time.time()
    print("result:",s.findMaximumXORHash(nums1))
    timeStamp3 = time.time()
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)

if __name__ == '__main__':
    main()
