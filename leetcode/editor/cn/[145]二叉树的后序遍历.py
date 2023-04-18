# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 574 👎 0

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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        op_satck = [0]
        while stack:
            if op_satck[-1] == 0:
                op_satck[-1] = 1
                node = stack[-1]
                if node.right:
                    stack.append(node.right)
                    op_satck.append(0)
                if node.left:
                    stack.append(node.left)
                    op_satck.append(0)
            else:
                res.append(stack.pop().val)
                op_satck.pop()
        return res

# leetcode submit region end(Prohibit modification and deletion)
