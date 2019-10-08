#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
# https://leetcode-cn.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (61.28%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 34.1K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用栈实现队列的下列操作：
# 
# 
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 
# 
# 示例:
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
# 
# 说明:
# 
# 
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.insert(0, x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            self.s1tos2()
        return self.s2.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            self.s1tos2()
        return self.s2[0]

    def s1tos2(self) -> None:
        while self.s1:
            self.s2.insert(0, self.s1.pop(0))

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
