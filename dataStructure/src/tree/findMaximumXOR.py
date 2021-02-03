#!/usr/bin/env python3

import collections

from myTrie import Trie

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)
        self.idx = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.dicl = ['0','1']
    def insertTrie(self, nums):
        #按位字典树:
        for num in nums:
            node = self.root
            print("insert num:", num)
            """
            for bit in '{:032b}'.format(num):
                node = node.children[bit]
                #print( bit, node)
            #print(node)
            """
            for idx in range(8,-1,-1):
                pre = node
                node.idx = idx
                val = num >> idx & 1
                node = node.children[str(val)]
                print(idx,val,pre.idx,pre,list(pre.children))
            node.isEnd = True
            print(pre.isEnd,node.isEnd,pre,node,list(node.children))
    def findHeadDFS(self, root):
        if not root:
            return self.root
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.children:
                count = len(cur.children)
                print(cur,count)
                if 2 > count:
                    for s in self.dicl:
                        if s in cur.children:
                            pre = cur
                            stack.append(cur.children[s])
                else:
                    break
        #return pre 
        return cur
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
        #xorNum = (xorNum << 1) | 1
        while cur:
            val = num >> cur.idx & 1
            tmp = 'x'
            print(cur.idx,cur.isEnd,val,end='|')
            if 0 == val:
                if cur.children['1']:
                    cur = cur.children['1']
                    xorNum = (xorNum << 1) | 1
                    tmp = 'a'
                else:
                    cur = cur.children['0']
                    xorNum <<= 1
                    tmp = 'b'
            else:
                if cur.children['0']:
                    cur = cur.children['0']
                    xorNum = (xorNum << 1) | 1
                    tmp = 'c'
                else:
                    cur = cur.children['1']
                    xorNum <<= 1
                    tmp = 'd'
            print(tmp,xorNum,end='|')
            if 0 == cur.idx:
                break
            #xorNum = max(xorNum, num ^ cur.idx )
        print(xorNum)
        return xorNum
    #def findMaximumXOR(self, nums: List[int]) -> int:
    def findMaximumXOR(self, nums):
        trie = self.root
        self.insertTrie(nums)
        # 贪心 找到最高位1 即可保证xor最大
        head = self.findHeadDFS(trie)
        print(head)
        self.searchMaxXOR(head,nums)
    def traversal(self):
        t = Trie()
        t.root = self.root
        diclist = ['1','0']
        print(t.traversalTrieLevel(t.root, diclist))
        print(t.traversalTrieFlagIter(t.root, diclist,"level"))
        #print(t.traversalTrieDFS(t.root, diclist))

def main():
    s = Solution()
    #nums1 = [3, 10, 5, 25, 2, 8]
    nums1 = [2,3,5,8,10,25]
    print(s.findMaximumXOR(nums1))

    print(s.traversal())

if __name__ == '__main__':
    main()
