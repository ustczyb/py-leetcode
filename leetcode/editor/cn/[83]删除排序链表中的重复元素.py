#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (47.82%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    47.8K
# Total Submissions: 99.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        cur_val = None
        pre = head
        while cur:
            val = cur.val
            next = cur.next
            if val != cur_val:
                pre = cur
                cur = next
                cur_val = val
            else:
                while next and next.val == val:
                    next = next.next
                if not next:
                    pre.next = next
                    break
                else:
                    cur.next = next.next
                    cur.val = next.val
        return head
                
# @lc code=end

