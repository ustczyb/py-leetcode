# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。 
# 
#  示例: 
# 
#  输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6 
#  Related Topics 堆 链表 分治算法


from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        head = ListNode(-1)
        tail = head
        count = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1
        while heap:
            _, _, node_p = heapq.heappop(heap)
            # 添加到链表中
            tail.next = node_p
            tail = node_p
            # 补充下一个元素到堆中
            if node_p.next:
                heapq.heappush(heap, (node_p.next.val, count, node_p.next))
                count += 1
        return head.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(4)
    a3 = ListNode(5)
    a1.next = a2
    a2.next = a3
    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3
    c1 = ListNode(2)
    c2 = ListNode(6)
    c1.next = c2
    res = Solution().mergeKLists([a1, b1, c1])
    while res:
        print(res.val)
        res = res.next
