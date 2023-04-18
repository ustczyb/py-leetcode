# 对链表进行插入排序。 
# 
#  
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。 
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。 
# 
#  
# 
#  插入排序算法： 
# 
#  
#  插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
#  每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 
#  重复直到所有输入数据插入完为止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2： 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#  
#  Related Topics 排序 链表 
#  👍 401 👎 0

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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode()
        new_head.next = head

        prev = head
        cur = prev.next

        def insert(prev, cur):
            p = new_head
            while p.next != cur:
                if p.next.val > cur.val:
                    prev.next = cur.next
                    cur.next = p.next
                    p.next = cur
                    return
                p = p.next

        while cur:
            next = cur.next
            insert(prev, cur)
            if prev.next != next:
                prev = prev.next
            cur = next
        return new_head.next

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # 4->2->1->3
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    p = Solution().insertionSortList(l1)
    while p:
        print(p.val)
        p = p.next