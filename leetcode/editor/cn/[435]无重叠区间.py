# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。 
# 
#  注意: 
# 
#  
#  可以认为区间的终点总是大于它的起点。 
#  区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。 
#  
# 
#  示例 1: 
# 
#  
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
#  Related Topics 贪心 数组 动态规划 排序 
#  👍 453 👎 0

# 这题想复杂了 我想的是根据区间重叠情况建一个图 然后根据图中各顶点的度数建堆 依次移除堆顶元素 直到图为孤立点
import functools
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def sort_rule(x, y):
            if x[1] < y[1]:
                return -1
            elif x[1] == y[1]:
                return 0
            else:
                return 1
        sorted_intervals = sorted(intervals, key=functools.cmp_to_key(sort_rule))
        res_intervals = []
        for interval in sorted_intervals:
            if not res_intervals:
                res_intervals.append(interval)
            else:
                if interval[0] >= res_intervals[-1][1]:
                    res_intervals.append(interval)
        return len(intervals) - len(res_intervals)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]]))