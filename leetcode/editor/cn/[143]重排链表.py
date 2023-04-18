# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ， 
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  示例 1: 
# 
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3. 
# 
#  示例 2: 
# 
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3. 
#  Related Topics 链表 
#  👍 572 👎 0

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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        new_head = ListNode()
        new_head.next = head
        # 找到链表中间节点 断开链表
        slow, fast = new_head, new_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_head = slow.next
        slow.next = None
        # 后半段链表逆序
        new_half_head = ListNode()
        new_half_head.next = mid_head
        p = mid_head.next
        while p:
            mid_head.next = p.next
            p.next = new_half_head.next
            new_half_head.next = p
            p = mid_head.next
        # 合并两段链表
        p1 = new_head.next
        p2 = new_half_head.next
        while p2:
            p1_next = p1.next
            p2_next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p1_next
            p2 = p2_next
        return new_head.next
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    p = Solution().reorderList(n1)
    while p:
        print(p.val)
        p = p.next