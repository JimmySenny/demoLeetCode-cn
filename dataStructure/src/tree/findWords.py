#!/usr/bin/env python3

import collections

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)
        self.word = None

class Solution:
    def __init__(self):
        self.diclist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):
        root = TrieNode()
        rowNum = len(board)
        if 0 == rowNum:
            return []
        colNum = len(board[0])
        res = []
        vis = [['F' for _ in range(colNum)] for _ in range(rowNum)]
        # 构造字典树
        for word in words:
            self.insertTrie(root,word)
            pass
        print("root:",list(root.children))
        print("trie:",self.traversalTrieDFS(root,self.diclist))
        # DFS搜索是否存在
        trie = root
        for row in range(rowNum):
            for col in range(colNum):
                print("main:",row,col,board[row][col],list(trie.children))
                if board[row][col] in trie.children:
                    self.matchDFS(board,row,col,trie,vis,res)
        print("result:",res)
        print("trie:",self.traversalTrieDFS(root,self.diclist))
        self.printMatrix(board,rowNum,colNum)
        self.printMatrix(vis,rowNum,colNum)
        return res
    def insertTrie(self, root, word):
        """ Inserts a word into the trie.  """
        node = root
        for c in word:
            node = node.children[c]
        node.isEnd = True
        node.word = word
                
    def matchDFS(self,board,row,col,trieNode,vis,res):
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        letter = board[row][col]
        print("--match0:",row,col,letter,list(trieNode.children),trieNode.isEnd)

        if letter not in trieNode.children:
            return 
        else:
            trieNode = trieNode.children[letter]
        print("--trie:",list(trieNode.children))
        print("--isEnd:",trieNode.isEnd)
        if trieNode.isEnd:
            res.append(trieNode.word)
            print("res:",res)
            return

        vis[row][col] = 'T'
        for i,j in directions:
            rowNew = row + i
            colNew = col + j
            if rowNew>=len(board) or rowNew<0 or colNew>=len(board[0]) or colNew<0:
                continue
            print("----vis:",rowNew,colNew,vis[rowNew][colNew])
            if 'T' == vis[rowNew][colNew]:
                continue
            c = board[rowNew][colNew]
            if c in trieNode.children:
                print("----dire:",c,rowNew,colNew,list(trieNode.children))
                vis[rowNew][colNew] = 'T'
                self.matchDFS(board,rowNew,colNew,trieNode,vis,res)
                vis[rowNew][colNew] = 'F'
        #vis[row][col] = 'F'

    def printMatrix(self,matrix,row,col):
        for i in range(row):
            print(matrix[i])

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


def main():
    s = Solution()
    #board = [["a","b"],["d","c"]]
    #words = ["bc"]

    #board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    #words = ["oath","pea","eat","rain"]

    #board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    #words = ["oa","oaa"] 
    # error oa oaa
    #board = [["a","a"]]
    #words = ["a"]
    # ["a"]
    board = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
    # error ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
    s.findWords(board,words)

if __name__ == '__main__':
    main()


