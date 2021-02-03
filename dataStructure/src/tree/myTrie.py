#!/usr/bin/env python3

import collections

"""
可以将字典树理解成一个个相连接的字典，在本题目中可以理解为一层最多有26个节点，
每个节点互不相同
"""

""" cpp 定义
class TrieNode{
    bool isEnd
    TrieNode* next[26]
}
"""

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        """ Initialize your data structure here.  """
        self.root = TrieNode()
        self.diclist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #def insert(self, word: str) -> None:
    def insert(self, word):
        """ Inserts a word into the trie.  """
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True

    #def search(self, word: str) -> bool:
    def search(self, word):
        """ Returns if the word is in the trie.  """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.isEnd

    #def startsWith(self, prefix: str) -> bool:
    def startsWith(self, prefix):
        #Returns if there is any word in the trie that starts with the given prefix.
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
    #def replaceWord(self, s: str) -> str:
    def replaceWord(self, s):
        node = self.root
        ss = ""
        for c in s:
            if c in node.children:
                node = node.children[c]
                ss += c
                #print("s,c,ss",s,c,ss)
                if node.isEnd:
                    return ss
            else:
                break
        return s
    """
    def traversalTrieRecursion(self,root,order="pre"):
        if not root:
            return []
        if "pre" == order:
            res = root.children
    """
    def traversalTrieDFS(self,root,diclist):
        if not root:
            return []
        stack = [root]
        res = []
        tmp = []
        while stack:
            cur = stack.pop()
            if cur.children:
                for s in diclist:
                    if s in cur.children:
                        tmp.append(s)
                        stack.append(cur.children[s])
            if cur.isEnd:
                res.append(list(tmp))
                tmp = []
        return res

    def traversalTrieLevel(self,root,diclist):
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            lay, layval = [], []
            #print("lay",cur)
            for node in cur:
                #print(list(node.children))
                if node.children:
                    layval.append(list(node.children.keys()))
                    for s in diclist:
                        if s in node.children:
                            #print(s,list(node.children))
                            lay.append(node.children[s])
            cur = lay
            if layval:
                res.append(layval)
        return res
    def traversalTrieFlagIter(self,root,diclist,order):
        if not root:
            return []
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
                if "pre" == order:
                    if cur.children:
                        for s in cur.children:
                            qs.append((0,cur.children[s]))
                        """
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                        """
                    qs.append((1,cur))
                if "post" == order:
                    qs.append((1,cur))
                    if cur.children:
                        for s in cur.children:
                            qs.append((0,cur.children[s]))
                        """
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                        """
                if "level" == order:
                    qs.append((1,cur))
                    if cur.children:
                        for s in cur.children:
                            qs.append((0,cur.children[s]))
                        """
                        for i in range(len(cur.children)):
                            qs.append((0,cur.children[i]))
                        """
            else:
                #print(list(cur.children))
                if cur.children:
                    res.append(list(cur.children))
        return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    obj = Trie()
    obj.insert("apple")
    obj.insert("apply")
    print("search:",obj.search("apple"))
    print("search:",obj.search("banana"))
    print("startsWith:",obj.startsWith("app"))
    print("startsWith:",obj.startsWith("b"))

    print(obj.traversalTrieDFS(obj.root, obj.diclist))
    print(obj.traversalTrieLevel(obj.root, obj.diclist))
    print(obj.traversalTrieFlagIter(obj.root, obj.diclist, "pre"))
    print(obj.traversalTrieFlagIter(obj.root, obj.diclist, "post"))
    print(obj.traversalTrieFlagIter(obj.root, obj.diclist, "level"))

if __name__ == '__main__':
    main()


