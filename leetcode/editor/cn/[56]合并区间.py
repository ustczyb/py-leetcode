# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  示例 1: 
# 
#  输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
#  Related Topics 排序 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        point_arr = []
        for region in intervals:
            point_arr.append((region[0], -1))
            point_arr.append((region[1], 1))
        point_arr.sort()
        cur_value = 0
        cur_start_value, cur_end_value = 0, 0
        for point, value in point_arr:
            if cur_value == 0:
                cur_start_value = point
                cur_value += value
                continue
            cur_value += value
            cur_end_value = point
            if cur_value == 0:
                res.append([cur_start_value, cur_end_value])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = [[1, 4], [4, 6]]
    print(Solution().merge(a))
