# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。 
# 
#  你应当 保留 两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 200] 内 
#  -100 <= Node.val <= 100 
#  -200 <= x <= 200 
#  
#  Related Topics 链表 双指针 
#  👍 393 👎 0

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
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return head

        less_head = ListNode()
        less_tail = less_head

        new_head = ListNode()
        new_head.next = head
        prev = new_head
        cur = head

        while cur:
            if cur.val < x:
                prev.next = cur.next
                cur.next = None
                less_tail.next = cur
                less_tail = less_tail.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

        less_tail.next = new_head.next
        return less_head.next

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(1)
    n1.next = n2
    p = Solution().partition(n1, 2)
    while p:
        print(p.val)
        p = p.next