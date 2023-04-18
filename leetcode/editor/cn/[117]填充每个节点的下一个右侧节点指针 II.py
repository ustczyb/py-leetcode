# 给定一个二叉树 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指
# 针连接），'#' 表示每层的末尾。 
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数小于 6000 
#  -100 <= node.val <= 100 
#  
# 
#  
# 
#  
#  
#  Related Topics 树 深度优先搜索 
#  👍 412 👎 0

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        queue2 = []
        while queue or queue2:
            while queue:
                node = queue.pop(-1)
                if queue:
                    node.next = queue[-1]
                if node.left:
                    queue2.insert(0, node.left)
                if node.right:
                    queue2.insert(0, node.right)
            while queue2:
                node = queue2.pop(-1)
                if queue2:
                    node.next = queue2[-1]
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
        return root

        # 降低空间复杂度
# leetcode submit region end(Prohibit modification and deletion)
