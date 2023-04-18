#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (62.71%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    26.8K
# Total Submissions: 42.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
# from typing import List

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        cur_layer = [root]
        while cur_layer:
            layer = []
            next_layer = []
            while cur_layer:
                node = cur_layer.pop(0)
                if node:
                    layer.append(node.val)
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            cur_layer = next_layer
            if layer:
                res.append(layer)
        return list(reversed(res))

# @lc code=end
# if __name__ == "__main__":
#     l = [1, 2, 3]
#     # print(list(reversed(l)))
#     print(l.pop(0))
