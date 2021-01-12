#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
#    def preorderTraversal(self, root: TreeNode) -> List[int]:
    def preorderTraversal(self, root):
# recursion1 递归1
        if not root:
            return []
        # 前序递归
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归 
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def inorderTraversal(self, root):
# 在树的深度优先遍历中（包括前序、中序、后序遍历），递归方法最为直观易懂，但考虑到效率，我们通常不推荐使用递归。
# 栈迭代方法虽然提高了效率，但其嵌套循环却非常烧脑，不易理解，容易造成“一看就懂，一写就废”的窘况。而且对于不同的遍历顺序（前序、中序、后序），循环结构差异很大，更增加了记忆负担。
# 因此，我在这里介绍一种“颜色标记法”（瞎起的名字……），兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。
# 其核心思想如下：
#   使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
#   如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
#   如果遇到的节点为灰色，则将节点的值输出。
# 我们有一棵二叉树：
#   前序遍历：中，左，右
#   中序遍历：左，中，右
#   后序遍历：左，右，中
# 栈是一种 先进后出的结构，出栈顺序为左，中，右 那么入栈顺序必须调整为倒序，也就是右，中，左 
#   同理，如果是前序遍历，入栈顺序为 右，左，中；后序遍历，入栈顺序中，右，左
        stack = [(0,root)]
        res = []
        while stack:
            flag, node = stack.pop()
            if node is None:
                continue;
            if 0 == flag:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:
                res.append(node.val)
        return res;



def main():
    s = Solution()
    node20 = TreeNode(20)
#    node10 = TreeNode(10,node20)
    node11 = TreeNode(11,node20)
    root = TreeNode(0,None,node11)

    print(s.inorderTraversal(root));
    print(s.preorderTraversal(root));

if __name__ == '__main__':
    main()
