#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (49.37%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 13.9K
# Testcase Example:  '0'
#
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# 
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 
# 
# 
# 例如，上面的二进制手表读取 “3:25”。
# 
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
# 
# 案例:
# 
# 
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]
# 
# 
# 
# 注意事项:
# 
# 
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for i in range(min(4, num + 1)):
            hours = self.readHour(i)
            mins = self.readMinute(num - i)
            res.extend(self.combine(hours, mins))
        return res

    def readHour(self, num: int) -> List[str]:
        if num == 0:
            return ['0']
        if num == 1:
            return ['1', '2', '4', '8']
        if num == 2:
            return ['3', '5', '6', '9', '10']
        if num == 3:
            return ['7', '11']
        else:
            return []
    
    def readMinute(self, num: int) -> List[str]:
        if num == 0:
            return ['00']
        if num == 1:
            return ['01','02','04','08','16','32']
        if num == 2:
            return [str(x)  for x in ['03','05','09',17,33,'06',10,18,34,12,20,36,24,40,48]]
        if num == 3:
            return [str(x)  for x in ['07',11,19,35,13,21,37,25,41,49,14,22,38,26,42,50,28,44,52,56]]
        if num == 4:
            return [str(x)  for x in [15,23,39,27,43,51,29,45,53,57,30,46,54,58]]
        if num == 5:
            return [str(x)  for x in [31,47,55,59]]
        else:
            return []

    def combine(self, hours: List[str], mins: List[str]) -> List[str]:
        res = []
        for h in hours:
            for m in mins:
                res.append(h + ':' + m)
        return res
# @lc code=end
if __name__ == "__main__":
    print(Solution().readBinaryWatch(3))