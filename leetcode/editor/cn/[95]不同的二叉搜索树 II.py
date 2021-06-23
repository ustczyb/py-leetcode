# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。 
# 
#  
# 
#  示例： 
# 
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 8 
#  
#  Related Topics 树 动态规划 
#  👍 859 👎 0

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

    def __init__(self):
        self.cache = {}
        self.cache[0] = [None]
        self.cache[1] = [TreeNode(1)]

    def tree_add_num(self, root: TreeNode, num: int):
        if not root:
            return
        new_root = TreeNode(root.val + num)
        new_root.left = self.tree_add_num(root.left, num)
        new_root.right = self.tree_add_num(root.right, num)
        return new_root

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n in self.cache:
            return self.cache[n]
        res = []
        for i in range(1, n + 1):
            for left_tree in self.generateTrees(i - 1):
                for right_tree in self.generateTrees(n - i):
                    root = TreeNode(i)
                    root.left = self.tree_add_num(left_tree, 0)
                    root.right = self.tree_add_num(right_tree, i)
                    res.append(root)
        self.cache[n] = res
        return res
# leetcode submit region end(Prohibit modification and deletion)
