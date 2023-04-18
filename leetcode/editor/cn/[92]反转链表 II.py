# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 878 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head: ListNode, tail: ListNode):
        # 翻转head到tail之间(不含两个端点)的节点
        p = head.next
        q = p.next
        while q != tail:
            # 头插法把q插入到表头
            p.next = q.next
            q.next = head.next
            head.next = q

            q = p.next
        return head


    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        left_node = h
        for i in range(left - 1):
            left_node = left_node.next
        right_node = h
        for i in range(right + 1):
            right_node = right_node.next
        self.reverse(left_node, right_node)
        return h.next
# leetcode submit region end(Prohibit modification and deletion)
