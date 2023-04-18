# 有效数字（按顺序）可以分成以下几个部分： 
# 
#  
#  一个 小数 或者 整数 
#  （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
#  
# 
#  小数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  下述格式之一：
#  
#  至少一位数字，后面跟着一个点 '.' 
#  至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
#  一个点 '.' ，后面跟着至少一位数字 
#  
#  
#  
# 
#  整数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  至少一位数字 
#  
# 
#  部分有效数字列举如下： 
# 
#  
#  ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
#  "53.5e93", "-123.456e789"] 
#  
# 
#  部分无效数字列举如下： 
# 
#  
#  ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] 
#  
# 
#  给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "0"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "e"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "."
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = ".1"
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。 
#  
#  Related Topics 数学 字符串 
#  👍 262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] in ['e', 'E']:
                return i < (len(s) - 1) and self.isInteger(s[i + 1:]) and (self.isInteger(s[:i]) or self.isDecimal(s[:i]))
        return self.isInteger(s) or self.isDecimal(s)

    def isInteger(self, s: str) -> bool:
        if not s:
            return False
        if len(s) > 1:
            for i in range(1, len(s)):
                if not s[i].isdigit():
                    return False
            if s[0].isdigit():
                return True
            if s[0] in ['+', '-']:
                return True
            return False
        return s[0].isdigit()

    def isDecimal(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ['-', '+']:
            s = s[1:]
        if len(s) < 2:
            return False
        if '.' not in s:
            return False
        split_arr = s.split('.')
        if len(split_arr) > 2:
            return False
        for sub_s in split_arr:
            if sub_s and not sub_s.isdigit():
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # for s in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    # for s in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] :
    print(Solution().isNumber('+.'))