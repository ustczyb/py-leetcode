# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 由小写英文字母组成 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 30
#  words[i] 由小写英文字母组成
#  
#  Related Topics 哈希表 字符串 滑动窗口 
#  👍 528 👎 0

from typing import List
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        target_len = len(words) * word_len
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1

        def matches(word):
            cur_word_dict = defaultdict(int)
            for i in range(0, target_len, word_len):
                cur_word = word[i: i + word_len]
                cur_word_dict[cur_word] += 1
                if cur_word_dict[cur_word] > word_dict[cur_word]:
                    return False
            return True

        result = []
        for start_index in range(len(s) - target_len + 1):
            if matches(s[start_index: start_index + target_len]):
                result.append(start_index)
        return result


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    print(Solution().findSubstring(s, words))
