# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 
# 
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：[3] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2] 
# 
#  
# 
#  提示： 
#  摩尔投票法
#  
#  1 <= nums.length <= 5 * 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics 数组 
#  👍 375 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums) < 3:
        #     return nums
        candidate1 = nums[0]
        candidate1_cnt = 1

        start_index = len(nums)
        for i in range(1, len(nums)):
            if nums[i] == candidate1:
                candidate1_cnt += 1
            else:
                candidate2 = nums[i]
                candidate2_cnt = 1
                start_index = i
                break

        for j in range(start_index + 1, len(nums)):
            if nums[j] == candidate1:
                candidate1_cnt += 1
            elif nums[j] == candidate2:
                candidate2_cnt += 1
            else:
                if candidate1_cnt == 0:
                    candidate1 = nums[j]
                    candidate1_cnt = 1
                elif candidate2_cnt == 0:
                    candidate2 = nums[j]
                    candidate2_cnt = 1
                else:
                    candidate1_cnt -= 1
                    candidate2_cnt -= 1

        candidate1_cnt, candidate2_cnt = 0, 0
        for num in nums:
            if num == candidate1:
                candidate1_cnt += 1
            elif num == candidate2:
                candidate2_cnt += 1

        res = []
        if candidate1_cnt > int(len(nums) / 3):
            res.append(candidate1)
        if candidate2_cnt > int(len(nums) / 3):
            res.append(candidate2)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1]
    print(Solution().majorityElement(nums))
