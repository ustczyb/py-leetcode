# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。 
# 
#  示例 1: 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2: 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5 
#  Related Topics 排序 链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        return self.mergeSortList(h1, h2)

    def mergeSortList(self, h1: ListNode, h2: ListNode) -> ListNode:
        h = ListNode(-1)
        cur = h
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        return h.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    res = Solution().sortList(n1)
    while res:
        print(res.val)
        res = res.next
