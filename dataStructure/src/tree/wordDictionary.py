#!/usr/bin/env python3

import collections

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)

from myTrie import Trie as Trie

class WordDictionary:
    def __init__(self):
        """ Initialize your data structure here.  """
        self.root = TrieNode()
    #def addWord(self, word: str) -> None:
    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True
    #def search(self, word: str) -> bool:
    def search(self, word):
        return self.searchDFS(word,self.root)
    def searchDFS(self, word, node):
        cur = node
        for i in range(len(word)):
            print("i,word[i]",i,word[i])
            """
            在遇到 '.' 的时候，使用递归方法，
            将该结点的每一个分支都看过去，只要有一个分支返回true 就可以了，
            全部分支都走过去，都没有返回 true 的才返回 false。
            """
            if '.' == word[i]:
                if cur.children:
                    for k in cur.children.keys():
                        print("k",k)
                        #当前k循环判断下一个字母是否符合匹配条件
                        if self.searchDFS(word[i+1:],cur.children[k]):
                            return True
                return False
            elif word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                return False
        return cur.isEnd
    def traversal(self):
        t = Trie()
        t.root = self.root
        return t.traversalTrieLevel(t.root, t.diclist)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def main():
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    obj.addWord("bcc")

    print("search:",obj.search("pad"))
    print("search:",obj.search("bad"))
    print("search:",obj.search(".ad"))
    print("search:",obj.search("b.."))
    print("search:",obj.search("..c"))
    print("search:",obj.search("..d"))
    print("search:",obj.search("..."))

    print(obj.traversal())

if __name__ == '__main__':
    main()
