# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。 
# 
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。 
# 
#  示例 3： 
# 
#  
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
#  
# 
#  示例 4： 
# 
#  
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
#  
# 
#  示例 5： 
# 
#  
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= intervals[i][0] <= intervals[i][1] <= 105 
#  intervals 根据 intervals[i][0] 按 升序 排列 
#  newInterval.length == 2 
#  0 <= newInterval[0] <= newInterval[1] <= 105 
#  
#  Related Topics 排序 数组 
#  👍 409 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        tmp = 0
        flag = 0
        start = -1
        end = -1
        if not intervals:
            res.append(newInterval)
            return res
        for i in range(len(intervals)):
            interval = intervals[i]
            if flag == 2:
                res.append(interval)
            if flag == 0:
                if interval[1] < newInterval[0]:
                    res.append(interval)
                elif interval[0] > newInterval[0]:
                    start = newInterval[0]
                    flag = 1
                    tmp += 2
                else:
                    start = interval[0]
                    flag = 1
                    tmp += 2
            if flag == 1:
                if interval[1] < newInterval[1]:
                    if i < len(intervals) - 1:
                        continue
                    else:
                        res.append([start, newInterval[1]])
                elif interval[0] > newInterval[1]:
                    end = newInterval[1]
                    res.append([start, end])
                    flag = 2
                    res.append(interval)
                else:
                    end = interval[1]
                    res.append([start, end])
                    flag = 2

        if start == -1:
            res.append(newInterval)
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(Solution().insert(intervals, newInterval))