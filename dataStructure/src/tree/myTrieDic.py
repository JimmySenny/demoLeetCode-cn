#!/usr/bin/env python3

import collections
import time

class TrieDicNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieDicNode)
        self.idx = -1

class TrieDic:
    def __init__(self):
        """ Initialize your data structure here.  """
        self.root = TrieDicNode()
        self.diclist = ['a','b','c','d','e','f','g']
            #,'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def insert(self, word: str) -> None:
    #def insert(self, word):
        """ Inserts a word into the trie.  """
        node = self.root
        idx = 0
        print("insert:",node)
        for c in word:
            node.idx = idx
            print(c,idx,node.idx,node,node.children[c],list(node.children),end='|')
            node = node.children[c]
            print(idx,node.idx,node)
            idx += 1
        node.isEnd = True
    def insertReverse(self, word):
        node = self.root
        lenw = len(word)
        i = lenw
        print("insertReverse:",node)
        for idx in range(5,-1,-1):
            node.idx = idx
            c = word[abs(i-lenw)]
            print(c,idx,node.idx,node,node.children[c],list(node.children),end='|')
            node = node.children[word[abs(i - lenw)]]
            #node.idx = idx
            print(idx,node.idx,node)
            i += 1
        node.isEnd = True
    def iter(self):
        node = self.root
        print("head:",node.idx,node.isEnd,node,list(node.children),node.children)
        while node.children:
            for d in self.diclist:
                print("-",d,list(node.children),len(node.children),node)
                if d in node.children:
                    node = node.children[d]
                print("--:",node.idx,node.isEnd,node,list(node.children))
            print("while:",node.isEnd,node,list(node.children))
    def iterDFS(self):
        root = self.root
        stack = [root]
        print("head:",root.idx,root.isEnd,root,list(root.children))
        while stack:
            cur = stack.pop()
            if cur.children:
                print("==:",cur.idx,cur.isEnd,cur,list(cur.children))
                for d in self.diclist:
                    print("-",d,list(cur.children))
                    if d in cur.children:
                        stack.append(cur)
                    time.sleep(1)
                cur = cur.children[d]
            print("----:",cur.idx,cur.isEnd,cur,list(cur.children))
            print(stack)
            time.sleep(1)


def main():
    print("insert1")
    td1 = TrieDic()
    td1.insert("abcdefg")
    td1.insert("abcxyz")
    #td1.iter()

    """
    """

    print("insert2")
    td2 = TrieDic()
    td2.insertReverse("abcdefg")
    td2.insertReverse("abcxyz")
    #td2.iter()


if __name__ == '__main__':
    main()


