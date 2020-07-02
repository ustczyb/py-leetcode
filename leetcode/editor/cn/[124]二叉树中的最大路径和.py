# 给定一个非空二叉树，返回其最大路径和。 
# 
#  本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 
#        1
#       / \
#      2   3
# 
# 输出: 6
#  
# 
#  示例 2: 
# 
#  输入: [-10,9,20,null,null,15,7]
# 
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# 
# 输出: 42 
#  Related Topics 树 深度优先搜索

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_value = root.val
        self.maxSingleSubPathSum(root)
        return self.max_value

    def maxSingleSubPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_val = max(self.maxSingleSubPathSum(root.left), 0)
        right_val = max(self.maxSingleSubPathSum(root.right), 0)
        cur_val = root.val + left_val + right_val
        if self.max_value < cur_val:
            self.max_value = cur_val
        return root.val + max(left_val, right_val)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    t1 = TreeNode(-10)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    print(Solution().maxPathSum(t1))
