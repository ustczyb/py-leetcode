# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 深度优先搜索 数组 
#  👍 492 👎 0

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        head = postorder[-1]
        if len(inorder) == 1:
            return TreeNode(head)
        for i in range(len(inorder)):
            if inorder[i] == head:
                break
        h = TreeNode(head)
        if i > 0:
            h.left = self.buildTree(inorder[:i], postorder[:i])
        if i < len(inorder) - 1:
            h.right = self.buildTree(inorder[i + 1:], postorder[i: -1])
        return h
# leetcode submit region end(Prohibit modification and deletion)
