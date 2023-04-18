#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (51.95%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 21.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.sumOfLeft(root, False)

    def sumOfLeft(self, root: TreeNode, isLeft: bool) -> int:
        if not root:
            return 0
        if isLeft and self.isLeaf(root):
            return root.val
        return self.sumOfLeft(root.left, True) + self.sumOfLeft(root.right, False)

    def isLeaf(self, node: TreeNode) -> bool:
        if not node:
            return False
        return not node.left and not node.right
# @lc code=end

