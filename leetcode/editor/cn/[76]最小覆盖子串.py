# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。 
# 
#  示例： 
# 
#  输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC" 
# 
#  说明： 
# 
#  
#  如果 S 中不存这样的子串，则返回空字符串 ""。 
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:

    def get_dict(self, s: str) -> dict:
        count_dict = defaultdict(int)
        for ch in s:
            count_dict[ch] += 1
        return count_dict

    def minWindowV1(self, s: str, t: str, s_dict, t_dict):
        begin = 0
        end = len(s) - 1
        while begin < end:
            if s[begin] not in t_dict:
                s_dict[s[begin]] -= 1
                begin += 1
                continue
            if s[end] not in t_dict:
                s_dict[s[end]] -= 1
                end -= 1
                continue
            break
        if t_dict[s[begin]] == s_dict[s[begin]] and t_dict[s[end]] == s_dict[s[end]]:
            return s[begin:end + 1]
        if s_dict[s[end]] == t_dict[s[end]]:
            s_dict[s[begin]] -= 1
            return self.minWindowV1(s[begin + 1: end + 1], t, s_dict, t_dict)
        if t_dict[s[begin]] == s_dict[s[begin]]:
            s_dict[s[end]] -= 1
            return self.minWindowV1(s[begin: end], t, s_dict.copy(), t_dict)
        s_dict[s[end]] -= 1
        l1 = self.minWindowV1(s[begin: end], t, s_dict.copy(), t_dict)
        s_dict[s[end]] += 1
        s_dict[s[begin]] -= 1
        l2 = self.minWindowV1(s[begin + 1: end + 1], t, s_dict, t_dict)
        if len(l1) > len(l2):
            return l2
        else:
            return l1

    def contains_target(self, s_dict, t_dict):
        for ch in t_dict:
            if s_dict[ch] < t_dict[ch]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        s_dict = self.get_dict(s)
        t_dict = self.get_dict(t)
        for ch in t_dict:
            if s_dict[ch] < t_dict[ch]:
                return ""
        cur_dict = defaultdict(int)
        cur_dict[s[0]] += 1
        res = s
        start = 0
        end = 0
        while end < len(s):
            if self.contains_target(cur_dict, t_dict):
                while s[start] not in t_dict or cur_dict[s[start]] > t_dict[s[start]]:
                    cur_dict[s[start]] -= 1
                    start += 1
                if end - start + 1 < len(res):
                    res = s[start: end + 1]
                cur_dict[s[start]] -= 1
                start += 1
            else:
                end += 1
                if end < len(s):
                    cur_dict[s[end]] += 1
                else:
                    break
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().minWindow('ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country',
                               'ask_country'))
