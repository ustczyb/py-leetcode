# 给定一个二叉树，原地将它展开为一个单链表。 
# 
#  
# 
#  例如，给定二叉树 
# 
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6 
# 
#  将其展开为： 
# 
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6 
#  Related Topics 树 深度优先搜索

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'TreeNode:' + str(self.val)


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expand(self, root: TreeNode) -> (TreeNode, TreeNode):
        if not root.left and not root.right:
            return (root, root)
        if root.left:
            left_head, left_tail = self.expand(root.left)
            if root.right:
                right_head, right_tail = self.expand(root.right)
                root.left = None
                root.right = left_head
                left_tail.right = right_head
                return root, right_tail
            else:
                root.right = left_head
                root.left = None
                return root, left_tail
        else:
            right_head, right_tail = self.expand(root.right)
            root.right = right_head
            return root, right_tail

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.expand(root)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(4)
    # t5 = TreeNode(5)
    # t6 = TreeNode(6)
    t1.left = t2
    # t2.left = t3
    # t2.right = t4
    # t1.right = t5
    # t5.right = t6
    head, tail = Solution().expand(t1)
