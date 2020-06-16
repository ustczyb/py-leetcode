# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
# 
#  说明：不允许修改给定的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#  
# 
#  
# 
#  
# 
#  进阶： 
# 你是否可以不用额外空间解决此题？ 
#  Related Topics 链表 双指针

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        while True:
            if not p2 or not p2.next:
                print('no cycle')
                return
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        q = head
        while p1 != q:
            p1 = p1.next
            q = q.next
        return q


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p2
    print(Solution().detectCycle(p1).val)
