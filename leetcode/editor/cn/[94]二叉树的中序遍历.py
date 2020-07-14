# 给定一个二叉树，返回它的中序 遍历。 
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
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return 'TreeNode:' + str(self.val)
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if not root:
    #         return res
    #     res.extend(self.inorderTraversal(root.left))
    #     res.append(root.val)
    #     res.extend(self.inorderTraversal(root.right))
    #     return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.left = t3
    print(Solution().inorderTraversal(t1))
