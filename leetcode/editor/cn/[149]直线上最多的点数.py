# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。 
# 
#  示例 1: 
# 
#  输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#  
# 
#  示例 2: 
# 
#  输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6 
#  Related Topics 哈希表 数学 
#  👍 234 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        def cal_line_coef(p1, p2):
            if p2[0] == p1[0]:
                k = 'inf'
                w = p2[0]
                return '%s_%s' % (str(k), str(w))
            k = (p2[1] - p1[1]) / (p2[0] - p1[0])
            w = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])
            return '%s_%s' % (str(k), str(w))

        point_nums = len(points)
        line_dict = defaultdict(set)
        for i in range(point_nums):
            for j in range(i + 1, point_nums):
                point_i = points[i]
                point_j = points[j]
                line = cal_line_coef(point_i, point_j)
                line_dict[line].add('%d_%d' % (point_i[0], point_i[1]))
                line_dict[line].add('%d_%d' % (point_j[0], point_j[1]))

        max_value = 0
        for k in line_dict:
            if len(line_dict[k]) > max_value:
                max_value = len(line_dict[k])
        return max_value

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    input = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(input))