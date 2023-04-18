# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  进阶： 
# 
#  
#  你可以设计一个只使用常数额外空间的算法来解决此问题吗？ 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
#  
# 
#  示例 4： 
# 
#  
# 输入：head = [1], k = 1
# 输出：[1]
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  列表中节点的数量在范围 sz 内 
#  1 <= sz <= 5000 
#  0 <= Node.val <= 1000 
#  1 <= k <= sz 
#  
#  Related Topics 链表 
#  👍 1061 👎 0

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

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        # 头结点
        h = ListNode()
        h.next = head
        start_node = h
        end_node = h
        for i in range(k + 1):
            if end_node:
                end_node = end_node.next
            else:
                return head
        while True:
            self.reverse(start_node, end_node)
            for i in range(k):
                start_node = start_node.next
                if end_node:
                    end_node = end_node.next
                else:
                    return h.next
        return h.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    h = Solution().reverseKGroup(l1, 5)
    while h:
        print(h.val)
        h = h.next
