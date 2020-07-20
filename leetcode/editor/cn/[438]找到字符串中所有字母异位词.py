# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:

    def is_match(self, c_dict, p_dict):
        for ch in p_dict:
            if c_dict[ch] != p_dict[ch]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window_size = len(p)
        if len(s) < window_size:
            return res
        p_dict = defaultdict(int)
        cur_dict = defaultdict(int)
        for ch in p:
            p_dict[ch] += 1
        for ch in s[:window_size]:
            cur_dict[ch] += 1
        if self.is_match(cur_dict, p_dict):
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            cur_dict[s[i - 1]] -= 1
            cur_dict[s[i + window_size - 1]] += 1
            if s[i + window_size - 1] in p_dict and self.is_match(cur_dict, p_dict):
                res.append(i)
        return res


        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
