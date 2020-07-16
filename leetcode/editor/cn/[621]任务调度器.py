# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务
# 都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。 
# 
#  然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 
# 
#  你需要计算完成所有任务所需要的最短时间。 
# 
#  
# 
#  示例 ： 
# 
#  输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
#  
# 
#  提示： 
# 
#  
#  任务的总个数为 [1, 10000]。 
#  n 的取值范围为 [0, 100]。 
#  
#  Related Topics 贪心算法 队列 数组

from typing import List
from collections import defaultdict
from math import ceil


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_arr = [0] * 26
        for t in tasks:
            count_arr[ord(t) - ord('A')] += 1
        count_arr.sort()
        max_height = count_arr[25]
        task_nums = len(tasks)
        idle_slots = (max_height - 1) * n
        for i in range(25):
            idle_slots -= min(count_arr[i], max_height - 1)
        if idle_slots > 0:
            return idle_slots + task_nums
        else:
            return task_nums


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # tasks = ["A", "B", "C", "D", "A", "B", "V"]
    # tasks = ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D", "D", "D", "E", "F"]
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
