# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。 
# 
#  注意： 
# 
#  
#  给定的目标值 target 是一个浮点数 
#  你可以默认 k 值永远是有效的，即 k ≤ 总结点数 
#  题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值 
#  
# 
#  示例： 
# 
#  输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
# 
#     4
#    / \
#   2   5
#  / \
# 1   3
# 
# 输出: [4,3] 
# 
#  拓展： 
# 假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？ 
#  Related Topics 栈 树 深度优先搜索 二叉搜索树 双指针 二叉树 堆（优先队列） 
#  👍 85 👎 0

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
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
# leetcode submit region end(Prohibit modification and deletion)
