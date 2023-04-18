#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (60.06%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 26.9K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        paths = []
        def traverseTree(node: TreeNode, cur_path: str):
            if not node:
                return
            if cur_path:
                next_path = cur_path + ('->' + str(node.val))
            else:
                next_path = str(node.val)
            if not node.left and not node.right:
                paths.append(next_path)
                return
            traverseTree(node.left, next_path)
            traverseTree(node.right, next_path)

        if not root:
            return paths
        traverseTree(root, '')
        return paths
# @lc code=end

