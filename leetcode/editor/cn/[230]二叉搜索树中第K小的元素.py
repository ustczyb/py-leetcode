# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。 
# 
#  说明： 
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。 
# 
#  示例 1: 
# 
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1 
# 
#  示例 2: 
# 
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3 
# 
#  进阶： 
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？ 
#  Related Topics 树 二分查找

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'TreeNode:' + str(self.val)


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cur_index = 0
        return self.traverse(root, k)

    def traverse(self, root: TreeNode, k: int):
        if not root:
            return None
        if not root.left and not root.right:
            self.cur_index += 1
            if self.cur_index == k:
                return root.val
            return None
        left_res = self.traverse(root.left, k)
        if left_res is not None:
            return left_res
        self.cur_index += 1
        if self.cur_index == k:
            return root.val
        right_res = self.traverse(root.right, k)
        if right_res is not None:
            return right_res
        return None


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(4)
    n6 = TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n4.left = n6
    print(Solution().kthSmallest(n1, 4))
