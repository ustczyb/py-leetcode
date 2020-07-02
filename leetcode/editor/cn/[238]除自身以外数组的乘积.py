# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之
# 外其余各元素的乘积。 
# 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,4]
# 输出: [24,12,8,6] 
# 
#  
# 
#  提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。 
# 
#  说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  进阶： 
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。） 
#  Related Topics 数组

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pi = 1
        zero_num = 0
        for num in nums:
            if num == 0:
                zero_num += 1
            else:
                pi *= num
        for num in nums:
            if zero_num > 1:
                res.append(0)
            elif zero_num == 1:
                if num == 0:
                    res.append(pi)
                else:
                    res.append(0)
            else:
                res.append(int(pi / num))
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().productExceptSelf([0, 0]))
