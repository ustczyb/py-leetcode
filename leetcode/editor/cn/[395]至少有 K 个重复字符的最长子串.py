# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由小写英文字母组成 
#  1 <= k <= 105 
#  
#  Related Topics 递归 分治算法 Sliding Window 
#  👍 501 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import re
from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counter = defaultdict(int)
        bad_chars = []
        for ch in s:
            counter[ch] += 1
        for ch in counter:
            if counter[ch] < k:
                bad_chars.append(ch)
        if not bad_chars:
            return len(s)

        splited_arr = re.split('|'.join(bad_chars), s)
        max_len = 0
        for sub_str in splited_arr:
            sub_res = self.longestSubstring(sub_str, k)
            if max_len < sub_res:
                max_len = sub_res
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().longestSubstring("ababbc", 2))