# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序排列 
#  
#  Related Topics 链表 
#  👍 607 👎 0

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        p = new_head
        while p.next:
            if not p.next.next or p.next.val < p.next.next.val:
                p = p.next
            else:
                q = p.next
                while q.next and q.val == q.next.val:
                    q = q.next
                p.next = q.next
        return new_head.next
# leetcode submit region end(Prohibit modification and deletion).next

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(1)
    l1.next = l2
    res = Solution().deleteDuplicates(l1)
    while res:
        print(res.val)
        res = res.next