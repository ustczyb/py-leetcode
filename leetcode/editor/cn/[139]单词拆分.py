# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。 
# 
#  说明： 
# 
#  
#  拆分时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#  
# 
#  示例 2： 
# 
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
#  Related Topics 动态规划

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        word_set = set(wordDict)
        word_len_set = set([len(x) for x in word_set])
        min_len = min(word_len_set)
        dp = [0] * len(s)

        def get_res(sub_s):
            length = len(sub_s)
            if not dp[length - 1]:
                if length < min_len:
                    dp[length - 1] = -1
                    return dp[length - 1]
                for l in word_len_set:
                    if length < l:
                        continue
                    if length == l and sub_s in word_set:
                        dp[length - 1] = 1
                        break
                    if sub_s[length - l:] in word_set:
                        if get_res(sub_s[:length - l]) == 1:
                            dp[length - 1] = 1
                            break
                if not dp[length - 1]:
                    dp[length - 1] = -1
            return dp[length - 1]

        return get_res(s) == 1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
