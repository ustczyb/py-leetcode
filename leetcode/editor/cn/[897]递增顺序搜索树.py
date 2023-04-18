# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的取值范围是 [1, 100] 
#  0 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 198 👎 0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def mid_travel(root: TreeNode) -> List[TreeNode]:
            if not root:
                return []
            res = []
            res.extend(mid_travel(root.left))
            res.append(root)
            res.extend(mid_travel(root.right))
            return res

        node_list = mid_travel(root)
        for i in range(len(node_list) - 1):
            node = node_list[i]
            node.left = None
            node.right = node_list[i + 1]
        node_list[-1].left = None
        return node_list[0]
# leetcode submit region end(Prohibit modification and deletion)
