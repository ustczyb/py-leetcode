# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。 
# 
#  每个矩形由其左下顶点和右上顶点坐标表示，如图所示。 
# 
#  
# 
#  示例: 
# 
#  输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45 
# 
#  说明: 假设矩形面积不会超出 int 的范围。 
#  Related Topics 数学 
#  👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        horizen = [A, C, E, G]
        vertical = [B, D, F, H]
        sorted_hor = sorted(horizen)
        sorted_ver = sorted(vertical)
        if sorted_hor[1] == C or sorted_hor[1] == G or sorted_ver[1] == D or sorted_ver[1] == H:
            intersection = 0
        else:
            intersection = (sorted_hor[2] - sorted_hor[1]) * (sorted_ver[2] - sorted_ver[1])
        return (C - A) * (D - B) + (G - E) * (H - F) - intersection
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().computeArea(-5, 4, 0, 5, -3, -3, 3, 3))