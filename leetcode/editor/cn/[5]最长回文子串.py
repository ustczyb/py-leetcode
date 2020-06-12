# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_len = 0
        cur_str = ''
        n = len(s)
        if n < 2:
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        # 长为奇数的子串
        for i in range(1, n - 1):
            flag = False
            j = 0
            for j in range(1, min(i + 1, n - i)):
                if s[i + j] != s[i - j]:
                    flag = True
                    if cur_len < 2 * j - 1:
                        cur_len = 2 * j - 1
                        cur_str = s[i - j + 1: i + j]
                        break
                    else:
                        break
            if not flag:
                j += 1
                if cur_len < 2 * j - 1:
                    cur_len = 2 * j - 1
                    cur_str = s[i - j + 1: i + j]

        # 长为偶数的子串
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                j = 0
                flag = False
                for j in range(1, min(i + 1, n - i - 1)):
                    if s[i - j] != s[i + 1 + j]:
                        flag = True
                        if cur_len < 2 * j:
                            cur_len = 2 * j
                            cur_str = s[i - j + 1: i + j + 1]
                            break
                        else:
                            break
                if not flag:
                    j += 1
                    if cur_len < 2 * j:
                        cur_len = 2 * j
                        cur_str = s[i - j + 1: i + j + 1]
        return cur_str


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print(Solution().longestPalindrome('babaddtattarrattatddetartrateedredividerb'))
