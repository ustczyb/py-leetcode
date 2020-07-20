# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 计算频数
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        heap = []
        for num in count_dict:
            if len(heap) < k:
                heapq.heappush(heap, count_dict[num])
            else:
                if count_dict[num] > heap[0]:
                    heapq.heapreplace(heap, count_dict[num])
        res = []
        for num in count_dict:
            if count_dict[num] >= heap[0]:
                res.append(num)
        return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
