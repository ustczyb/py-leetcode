# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑
# 充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。 
# 
#  示例 1: 
# 
#  输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: [[7,10],[2,4]]
# 输出: 1 
#  Related Topics 堆 贪心算法 排序

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = [x[0] for x in intervals]
        end_times = [x[1] for x in intervals]
        start_times.sort()
        end_times.sort()
        size = len(intervals)
        start_index, end_index = 0, 0
        cur_room, max_room = 0, 0
        while start_index < size and end_index < size:
            # 开始时没有会议结束
            if start_times[start_index] < end_times[end_index]:
                start_index += 1
                cur_room += 1
                max_room = cur_room if cur_room > max_room else max_room
            else:
                end_index += 1
                cur_room -= 1
        return max_room


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
