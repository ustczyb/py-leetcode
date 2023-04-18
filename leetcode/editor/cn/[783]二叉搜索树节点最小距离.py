# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bs
# t/ 相同 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [2, 100] 内 
#  0 <= Node.val <= 105 
#  差值是一个正数，其数值等于两值之差的绝对值 
#  
#  
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 185 👎 0

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
        self.min_diff = 200
        self.previous = None

    def midTraval(self, root: TreeNode):
        if root.left:
            self.midTraval(root.left)
        if self.previous and root.val - self.previous < self.min_diff:
            self.min_diff = root.val - self.previous
        self.previous = root.val
        if root.right:
            self.midTraval(root.right)

    def minDiffInBST(self, root: TreeNode) -> int:
        self.midTraval(root)
        return self.min_diff

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n1.left = n2
    n3 = TreeNode(6)
    n1.right = n3
    n4 = TreeNode(1)
    n2.left = n4
    n5 = TreeNode(3)
    n2.right = n5
    print(Solution().minDiffInBST(n1))