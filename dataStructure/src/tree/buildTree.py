#!/usr/bin/env python3

from traversal import Solution as tr
import time

# Definition for a binary tree root.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self,preorder,inorder):
        plen = len(preorder)
        ilen = len(inorder)
        if plen != ilen:
            raise Exception('数据输入错误')
        return self._build_tree(inorder, 0, ilen-1,preorder, 0, plen-1)
    """
     * 使用数组 preorder 在索引区间 [preLeft, preRight] 中的所有元素
     * 和数组 inorder 在索引区间 [inLeft, inRight] 中的所有元素构造二叉树
     *
     * @param preorder 二叉树前序遍历结果
     * @param preLeft  二叉树前序遍历结果的左边界
     * @param preRight 二叉树前序遍历结果的右边界
     * @param inorder  二叉树后序遍历结果
     * @param inLeft   二叉树后序遍历结果的左边界
     * @param inRight  二叉树后序遍历结果的右边界
     * @return 二叉树的根结点
    """
    def _build_tree(self,inorder,iLeft,iRight,preorder,pLeft,pRight):
        #递归终止条件
        if iLeft > iRight or pLeft > pRight:
            return None
        #前序的起点即为根
        rootVal = preorder[pLeft]
        root = TreeNode(rootVal)
        #根节点在中序中的位置
        index = iLeft
        print("iLeft,iRight,pLeft,pRight,rootVal",iLeft,iRight,pLeft,pRight,rootVal)
        while inorder[index] != rootVal and index <= iRight:
            print(index,inorder[index],end='|')
            index += 1
        print(index)
        #time.sleep(1)
        #ils = ils, ile = index -1
        #pls = pls + 1, ple = pls + index - ils(起始位置+ 长度index-ils)
        #irs = index + 1, ire = ire
        #prs = prs + index - ils + 1, pre = pre
        #从左子树递归
        root.left = self._build_tree(inorder,iLeft,index-1,preorder,pLeft+1,pLeft+index-iLeft)
        #从右子树递归
        root.right = self._build_tree(inorder,index+1,iRight,preorder,pLeft+index-iLeft+1,pRight)
        return root

    def buildTreeStack(self,preorder,inorder):
        """
        我们用一个栈保存已经遍历过的节点，遍历前序遍历的数组， 一直作为当前根节点的左子树，直到当前节点和中序遍历的数组的节点相等了，
        那么我们正序遍历中序遍历的数组，倒着遍历已经遍历过的根节点（用栈的 pop 实现）， 找到最后一次相等的位置，把它作为该节点的右子树。 如果满足 preoder[pre] == inorder[in] ,
        对判断左子树是否直接返回本身结束递归只需要看它的父亲是否满足父子颠倒（preoder[pre-1]
        == inorder[in+1]),
        但是对判断右子树就需要找到很久远的祖先的值才能确定是否能够直接 return,
        即(preorder[pre-n] == inorder[in+1] ), 所以左子树递归传父亲值，
        而右子树递归传祖先值。
        待研究
        """
        pLen = len(preorder)
        if 0 == pLen:
            return None
        #用一个栈保存已经遍历的节点，用 curRoot 保存当前正在遍历的节点。
        cur = TreeNode(preorder[0])
        nodeStack = [cur]
        root = cur
        p = 1
        i = 0
        # 遍历前序遍历的数组
        while (p < pLen):
            # 出现了当前节点的值和中序遍历数组的值相等，寻找是谁的右子树
            print("cur.val,i,i[i],p,p[p]", cur.val,i,inorder[i],p,preorder[p])
            if cur.val == inorder[i]:
                #每次进行出栈，实现倒着遍历
                while nodeStack and nodeStack[-1].val == inorder[i]:
                    cur = nodeStack.pop()
                    print("cur.val", cur.val,i,inorder[i])
                    i += 1
                # 设为当前的右孩子
                cur.right = TreeNode(preorder[p])
                print("right p,pval",cur.val,p,preorder[p])
                # 更新 cur
                cur = cur.right
                nodeStack.append(cur)
                p += 1
            else:
                # 否则的话就一直作为左子树
                cur.left = TreeNode(preorder[p])
                print("left p,pval",cur.val,p,preorder[p])
                cur = cur.left
                nodeStack.append(cur)
                p += 1
        return root

    # 可以将中序遍历的值和索引存在一个哈希表中
    # 这样就可以一下子找到根结点在中序遍历数组中的索引
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
        rootVal  = pre[prestart]
        index = inArrayMapList[rootVal]
        print("ins,ine,pres,pree,rootVal,i",instart,inend,prestart,preend,pre[prestart],index)
        root = TreeNode(rootVal)
        #ils = ils, ile = index -1
        #pls = pls + 1, ple = pls + index - ils(起始位置+ 长度index-ils)
        #irs = index + 1, ire = ire
        #prs = prs + index - ils + 1, pre = pre
        #递归构造左子树
        root.left = self.fromInPre(instart,index-1,prestart+1,prestart+index-instart, inArrayMapList,pre)
        #递归构造右子树
        root.right = self.fromInPre(index+1,inend,prestart+index-instart+1,preend, inArrayMapList,pre)
        return root

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
        rootVal  = post[postend]
        index = inArrayMapList[rootVal]
        print("ins,ine,posts,poste,rootVal,ri",instart,inend,poststart,postend,post[postend],index)
        root = TreeNode(rootVal)
        #ils = ils, ile = index -1
        #pls = pls, ple = pls + index - ils - 1(起始位置+ 长度index-ils -1 )
        #irs = index + 1, ire = ire
        #prs = prs + index - ils, pre = pre - 1
        #递归构造左子树
        root.left = self.fromInPost(instart,index-1,poststart,poststart+index-instart-1, inArrayMapList,post)
        #递归构造右子树
        root.right = self.fromInPost(index+1,inend,poststart+index-instart,postend-1, inArrayMapList,post)
        return root
def main():
    s = Solution()
    t = tr()
    preorder = [1,2,4,5,3,6,8,7]
    inorder = [4,2,5,1,6,8,3,7]
    postorder = [4,5,2,8,6,7,3,1]
    print(preorder)
    print(inorder)
    print(postorder)
    root = s.buildTree(preorder,inorder)
    print("pre:",t.traversalflagiter(root,"pre"))
    print("in:",t.traversalflagiter(root,"in"))
    print("post:",t.traversalflagiter(root,"post"))
    root1 = s.buildTreeFromInPre(preorder,inorder)
    print("pre:",t.traversalflagiter(root1,"pre"))
    print("in:",t.traversalflagiter(root1,"in"))
    print("post:",t.traversalflagiter(root1,"post"))
    root2 = s.buildTreeFromInPost(inorder,postorder)
    print("pre:",t.traversalflagiter(root2,"pre"))
    print("in:",t.traversalflagiter(root2,"in"))
    print("post:",t.traversalflagiter(root2,"post"))

    root3 = s.buildTreeStack(preorder,inorder)
    print("pre:",t.traversalflagiter(root3,"pre"))
    print("in:",t.traversalflagiter(root3,"in"))
    print("post:",t.traversalflagiter(root3,"post"))

if __name__ == '__main__':
    main()
