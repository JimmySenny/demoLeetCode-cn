#!/usr/bin/env python3

import collections

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)
        self.val = 0

class MapSum:
    def __init__(self):
        """ Initialize your data structure here.  """
        self.root = TrieNode()
    #def insert(self, key: str, val: int) -> None:
    def insert(self, key, val):
        """ Inserts a word into the trie.  """
        node = self.root
        for k in key:
            node = node.children[k]
        node.val = val
        node.isEnd = True
    #def sum(self, prefix: str) -> int:
    def sumx(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.children:
                print(node.children.keys())
                print(node.children.values())
                node = node.children[c]
            else:
                return 0
        print(node,node.children.items())
        print("prefix",prefix)
        ans = self.sumxDFS(node)
        print("ans:",ans)
        return ans
    def sumxDFS(self,root):
        if not root:
            return [0]
        stack = [root]
        ans = 0
        while stack:
            cur = stack.pop()
            if cur.isEnd:
                ans += cur.val
            if cur.children:
                stack.extend(cur.children.values())
        return ans

    #def search(self, word: str) -> bool:
    def search(self, prefix):
        """ Returns if the word is in the trie.  """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
                #print("c:val",c,node.val,node.isEnd)
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
    def traversalNTreeFlagIter(self,order):
        res = []
        qs = [(0,self.root)]
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
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                    qs.append((1,cur))
                if "post" == order:
                    qs.append((1,cur))
                    if cur.children:
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                if "level" == order:
                    qs.append((1,cur))
                    if cur.children:
                        for i in range(len(cur.children)):
                            qs.append((0,cur.children[i]))

                        """
                        for node in cur.children:
                            qs.append((0,node))
                        """
            else:
                #res.append(cur.children.items())
                print(cur.children.keys())
                print(cur.children.values())
        return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    obj = MapSum()
    obj.insert("ap",2)
    obj.insert("app",3)
    obj.insert("apple",5)
    obj.insert("apply",5)

    print("search:",obj.search("apple"))
    print("search:",obj.search("banana"))
    print("startsWith:",obj.startsWith("app"))
    print("startsWith:",obj.startsWith("b"))

    print("sum:",obj.sumx("a"))
    """
    print("sum:",obj.sumx("ap"))
    print("sum:",obj.sumx("app"))
    print("sum:",obj.sumx("appl"))
    """
    print("sum:",obj.sumx("apple"))
    print("sum:",obj.sumx("apply"))

    """
    print(obj.traversalNTreeFlagIter("pre"))
    print(obj.traversalNTreeFlagIter("post"))
    print(obj.traversalNTreeFlagIter("level"))
    """

if __name__ == '__main__':
    main()
