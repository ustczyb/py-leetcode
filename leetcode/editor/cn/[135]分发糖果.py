# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。 
# 
#  你需要按照以下要求，帮助老师给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。 
#  
# 
#  那么这样下来，老师至少需要准备多少颗糖果呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2： 
# 
#  
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。 
#  Related Topics 贪心算法 
#  👍 537 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        n = len(ratings)
        candies = [0] * n
        for i in range(n):
            # 低点置为1
            if i == 0 and ratings[i] <= ratings[i + 1]:
                candies[i] = 1
            elif i == n - 1 and ratings[i] <= ratings[i - 1]:
                candies[i] = 1
            elif ratings[i] < ratings[i - 1] and ratings[i] < ratings[i + 1]:
                candies[i] = 1
            # 相邻分数相等 置为1
            if i > 0 and i < n - 1:
                if ratings[i] == ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                    candies[i] = 1
                elif ratings[i] == ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                    candies[i] = 1
        for i in range(n):
            if candies[i] == 1:
                j = i
                while j > 0 and ratings[j - 1] > ratings[j] and candies[j - 1] < candies[j] + 1:
                    candies[j - 1] = candies[j] + 1
                    j -= 1
                j = i
                while j < n - 1 and ratings[j + 1] > ratings[j] and candies[j + 1] < candies[j] + 1:
                    candies[j + 1] = candies[j] + 1
                    j += 1
        print(candies)
        return sum(candies)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ratings = [1, 0]
    print(Solution().candy(ratings))
