#!/usr/bin/env python3

from traversal import Solution as tr
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTreeFromInPost(self, inorder, postorder):
        inArrayMapList = {}
        # 将节点值及索引全部记录在哈希表中
        for i in range(len(inorder)):
            inArrayMapList.setdefault(inorder[i],i)
        post = postorder
        return self.fromInPost(0,len(inorder)-1,0,len(post)-1,inArrayMapList,post)
    def fromInPost(self,instart,inend,poststart,postend,inArrayMapList,post):
        if instart > inend or poststart > postend:
            return None
        root  = post[postend]
        index = inArrayMapList[root]
        print("ins,ine,posts,poste,root,ri",instart,inend,poststart,postend,post[postend],index)
        node = TreeNode(root)
        #ils = ils, ile = index -1
        #pls = pls, ple = pls + index - ils - 1(起始位置+ 长度index-ils -1 )
        #irs = index + 1, ire = ire
        #prs = prs + index - ils, pre = pre - 1
        node.left = self.fromInPost(instart,index-1,poststart,poststart+index-instart-1, inArrayMapList,post)
        node.right = self.fromInPost(index+1,inend,poststart+index-instart,postend-1, inArrayMapList,post)
        return node
#    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTreeFromInPre(self, preorder,inorder):
        inArrayMapList = {}
        # 将节点值及索引全部记录在哈希表中
        for i in range(len(inorder)):
            inArrayMapList.setdefault(inorder[i],i)
        pre = preorder 
        return self.fromInPre(0,len(inorder)-1,0,len(pre)-1,inArrayMapList,pre)
    def fromInPre(self,instart,inend,prestart,preend,inArrayMapList,pre):
        if instart > inend or prestart > preend:
            return None
        root  = pre[prestart]
        index = inArrayMapList[root]
        print("ins,ine,pres,pree,root,i",instart,inend,prestart,preend,pre[prestart],index)
        time.sleep(1)
        node = TreeNode(root)
        #ils = ils, ile = index -1
        #pls = pls + 1, ple = pls + index - ils(起始位置+ 长度index-ils)
        #irs = index + 1, ire = ire
        #prs = prs + index - ils + 1, pre = pre
        node.left = self.fromInPre(instart,index-1,prestart+1,prestart+index-instart, inArrayMapList,pre)
        node.right = self.fromInPre(index+1,inend,prestart+index-instart+1,preend, inArrayMapList,pre)
        return node
            
def main():
    s = Solution()
    t = tr()
    preorder = [1,2,4,5,3,6,8,7]
    inorder = [4,2,5,1,6,8,3,7]
    postorder = [4,5,2,8,6,7,3,1]
    print(preorder)
    print(inorder)
    print(postorder)
    root1 = s.buildTreeFromInPost(inorder,postorder)
    print("pre:",t.traversalflagiter(root1,"pre"))
    print("in:",t.traversalflagiter(root1,"in"))
    print("post:",t.traversalflagiter(root1,"post"))

    root2 = s.buildTreeFromInPre(preorder,inorder)
    print("pre:",t.traversalflagiter(root2,"pre"))
    print("in:",t.traversalflagiter(root2,"in"))
    print("post:",t.traversalflagiter(root2,"post"))

if __name__ == '__main__':
    main()
