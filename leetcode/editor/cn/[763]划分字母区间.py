# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心 哈希表 双指针 字符串 
#  👍 526 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
import functools
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        if len(s) == 1:
            return [1]
        range_dict = defaultdict(list)
        for i in range(len(s)):
            ch = s[i]
            if ch not in range_dict:
                range_dict[ch].append(i)
                range_dict[ch].append(i)
            else:
                range_dict[ch][1] = i
        start = 0
        end = range_dict[s[0]][1]
        res = []
        while end < len(s):
            i = start + 1
            while i < end:
                ch = s[i]
                if range_dict[ch][1] > end:
                    end = range_dict[ch][1]
                i += 1
            res.append(end - start + 1)
            start = end + 1
            if start < len(s):
                end = range_dict[s[start]][1]
            else:
                break
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))