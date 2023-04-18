# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复
# 序列有时会对研究非常有帮助。 
# 
#  编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 105 
#  s[i] 为 'A'、'C'、'G' 或 'T' 
#  
#  Related Topics 位运算 哈希表 字符串 滑动窗口 哈希函数 滚动哈希 
#  👍 195 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # my solution: time: O((N - L)L)  space: O((N - L)L)
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     if len(s) <= 10:
    #         return []
    #     res = set()
    #     word_set = set()
    #     for start_index in range(len(s) - 9):
    #         word = s[start_index: start_index + 10]
    #         if word in word_set:
    #             res.add(word)
    #         else:
    #             word_set.add(word)
    #     return list(res)

    def __init__(self):
        self.vocab_dict = {
            'A': 0,
            'C': 1,
            'T': 2,
            'G': 3
        }
        self.len = 10
        self.vocab_size = 4
        self.max_weight = 4 ** (self.len - 1)

    def get_next_hash(self, cur_hash: int, last_ch, next_ch):
        return self.vocab_size * (cur_hash - self.max_weight * self.vocab_dict[last_ch]) + self.vocab_dict[next_ch]

    def hash(self, s: str) -> int:
        weight = 1
        res = 0
        for i in range(len(s)):
            ch = s[len(s) - 1 - i]
            res += self.vocab_dict[ch] * weight
            weight *= len(self.vocab_dict)
        return res

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_set = set()
        result = set()
        init_hash = self.hash(s[:self.len])
        for i in range(len(s) - self.len + 1):
            if init_hash in hash_set:
                result.add(s[i: i + self.len])
            else:
                hash_set.add(init_hash)
            if i < len(s) - self.len:
                init_hash = self.get_next_hash(init_hash, s[i], s[i + self.len])
        return list(result)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "AAAAAAAAAAA"
    print(Solution().findRepeatedDnaSequences(s))
