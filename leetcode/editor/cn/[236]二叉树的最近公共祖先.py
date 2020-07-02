# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#  
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉树中。 
#  
#  Related Topics 树

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p or root == q:
            return root
        path_to_p = self.findPath(root, p)
        path_to_q = self.findPath(root, q)
        print(path_to_p)
        print(path_to_q)
        max_path, min_path = (path_to_p, path_to_q) if len(path_to_p) > len(path_to_q) else (path_to_q, path_to_p)
        cur_node = root
        for i in range(len(min_path)):
            if not min_path[i] == max_path[i]:
                return cur_node
            else:
                cur_node = cur_node.left if min_path[i] == 1 else cur_node.right
        return cur_node

    def findPath(self, root: TreeNode, p: TreeNode) -> List[int]:
        if not root:
            return []
        if root.left == p:
            return [1]
        if root.right == p:
            return [2]
        sub_path = self.findPath(root.left, p)
        if sub_path:
            sub_path.insert(0, 1)
            return sub_path
        sub_path = self.findPath(root.right, p)
        if sub_path:
            sub_path.insert(0, 2)
            return sub_path
        return []


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(6)
    n5 = TreeNode(2)
    n6 = TreeNode(0)
    n7 = TreeNode(8)
    n8 = TreeNode(7)
    n9 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9
    print(Solution().lowestCommonAncestor(n1, n4, n6))
