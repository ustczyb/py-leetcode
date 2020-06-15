# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = ListNode(0)
        h.next = head
        p = h
        while p.next and p.next.next:
            cur = p.next
            cur_next = cur.next
            p.next = cur_next
            cur.next = cur_next.next
            cur_next.next = cur
            p = p.next.next
        return h.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    node_list = []
    for num in nums:
        node = ListNode(num)
        node_list.append(node)
    for i in range(len(node_list) - 1):
        node = node_list[i]
        node.next = node_list[i + 1]
    print(Solution().swapPairs(node_list[0]))
