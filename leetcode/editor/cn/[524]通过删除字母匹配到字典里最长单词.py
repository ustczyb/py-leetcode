# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。 
# 
#  如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 1000 
#  s 和 dictionary[i] 仅由小写英文字母组成 
#  
#  Related Topics 数组 双指针 字符串 排序 
#  👍 150 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:

    def isSubsequence(self, word: str, sentence: str) -> bool:
        word_index = sentence_index = 0
        while word_index < len(word) and sentence_index < len(sentence):
            if word[word_index] == sentence[sentence_index]:
                word_index += 1
                sentence_index += 1
            else:
                sentence_index += 1
        if word_index == len(word):
            return True
        else:
            return False

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        cur_word = ''
        for word in dictionary:
            if len(word) > len(cur_word):
                if self.isSubsequence(word, s):
                    cur_word = word
            if len(word) == len(cur_word) and word < cur_word:
                if self.isSubsequence(word, s):
                    cur_word = word
        return cur_word
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    print(Solution().findLongestWord(s, dictionary))