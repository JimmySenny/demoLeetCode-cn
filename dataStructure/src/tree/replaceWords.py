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
# python使用字典树实现
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)

from myTrie import Trie as Trie

class Solution:
    def __init__(self):
        self.root = Trie()
    #def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    def replaceWords(self, dictionary, sentence):
        print(dictionary,sentence)
        trie = self.root
        return self.proc(trie,self.initTrie(trie,dictionary),sentence)
    def initTrie(self,trie,dictionary):
        # 构建前缀树
        for i in range(len(dictionary)):
            print(dictionary[i],type(dictionary))
            trie.insert(str(dictionary[i]))
            pass
        return trie
    def proc(self, trie,dicroot,sentence):
        # 处理
        senarray = sentence.split()
        senlist = list(senarray)
        senlen = len(senlist)
        if 0 == senlen:
            return ""
        ans = ""
        for i in range(senlen):
            ans += trie.replaceWord(str(senlist[i]))
            ans += " "
        return ans

    def traversal(self):
        t = Trie()
        return 


def main():
    s = Solution()
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replaceWords(dictionary, sentence))

    s1 = Solution()
    dictionary1 = ["a", "aa", "aaa", "aaaa"]
    sentence1 = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    print(s1.replaceWords(dictionary1, sentence1))

    t = Trie()
    print(t.traversalTrieLevel(s.root.root,t.diclist))
    print(t.traversalTrieLevel(s1.root.root,t.diclist))

if __name__ == '__main__':
    main()
