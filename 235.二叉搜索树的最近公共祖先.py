#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (60.57%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 42.6K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 
# 
# 示例 2:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
# 
# 
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_to_p = list(reversed(self.pathTo(root, p)))
        root_to_q = list(reversed(self.pathTo(root, q)))
        p_len = len(root_to_p)
        q_len = len(root_to_q)
        if p_len > q_len:
            for i in range(q_len):
                p_cur = root_to_p[i]
                q_cur = root_to_q[i]
                if p_cur != q_cur:
                    return self.findNodeByPath(root, root_to_p[:i])
            return q
        else:
            for i in range(p_len):
                p_cur = root_to_p[i]
                q_cur = root_to_q[i]
                if p_cur != q_cur:
                    return self.findNodeByPath(root, root_to_p[:i])
            return p
        
    def findNodeByPath(self, root: 'TreeNode', path: List):
        if not path:
            return root
        res = root
        for i in path:
            if i == 'l':
                res = res.left
            if i == 'r':
                res = res.right
        return res

    def pathTo(self, root: 'TreeNode', target: 'TreeNode'):
        if root == target:
            return []
        if not root:
            return None
        l_path = self.pathTo(root.left, target)
        r_path = self.pathTo(root.right, target)
        if l_path != None:
            l_path.append('l')
            return l_path
        if r_path != None:
            r_path.append('r')
            return r_path
    

# @lc code=end

