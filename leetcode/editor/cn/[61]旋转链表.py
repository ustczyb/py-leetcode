# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#  
# 
#  示例 2: 
# 
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL 
#  Related Topics 链表 双指针


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode:' + str(self.val)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        p = head
        length = 1
        while p.next:
            length += 1
            p = p.next
        tail = p
        k = k % length
        if k == 0:
            return head
        mid = head
        for i in range(length - k - 1):
            mid = mid.next
        tail.next = head
        res = mid.next
        mid.next = None
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    print(Solution().rotateRight(n1, 1).val)
