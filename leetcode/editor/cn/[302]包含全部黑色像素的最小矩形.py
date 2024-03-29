# 图片在计算机处理中往往是使用二维矩阵来表示的。 
# 
#  给你一个二进制矩阵 image 表示一张黑白图片，0 代表白色像素，1 代表黑色像素。 
# 
#  黑色像素相互连接，也就是说，图片中只会有一片连在一块儿的黑色像素。像素点是水平或竖直方向连接的。 
# 
#  给你两个整数 x 和 y 表示某一个黑色像素的位置，请你找出包含全部黑色像素的最小矩形（与坐标轴对齐），并返回该矩形的面积。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y =
#  2
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：image = [["1"]], x = 0, y = 0
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == image.length 
#  n == image[i].length 
#  1 <= m, n <= 100 
#  image[i][j] 为 '0' 或 '1' 
#  1 <= x < m 
#  1 <= y < n 
#  image[x][y] == '1'. 
#  image 中的黑色像素仅形成一个 组件 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 二分查找 矩阵 
#  👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
# leetcode submit region end(Prohibit modification and deletion)
