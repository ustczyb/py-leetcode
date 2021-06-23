# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  说明: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  示例: 
# 
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
#  Related Topics 字符串 
#  👍 136 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        length_arr = [len(s) for s in words]
        res = []

        def make_single_line(word_indexes) -> str:
            word_nums = len(word_indexes)
            if word_nums == 1:
                return words[word_indexes[0]] + ' ' * (maxWidth - length_arr[word_indexes[0]])
            space_length = maxWidth - sum([length_arr[x] for x in word_indexes])
            mean_space = int(space_length / (word_nums - 1))
            left = space_length % (word_nums - 1)
            space_length_list = [mean_space + 1] * left + [mean_space] * (word_nums - 1 - left)
            res_str = ""
            for i in range(word_nums):
                res_str += words[word_indexes[i]]
                if i < word_nums - 1:
                    res_str += ' ' * space_length_list[i]
            return res_str

        cur_line_length = 0
        cur_line_word_indexes = []
        for i in range(len(words)):
            word = words[i]
            if cur_line_length + length_arr[i] + (0 if cur_line_length == 0 else 1) <= maxWidth:
                cur_line_word_indexes.append(i)
                cur_line_length += length_arr[i] + (0 if cur_line_length == 0 else 1)
            else:
                res.append(make_single_line(cur_line_word_indexes))
                cur_line_length = length_arr[i]
                cur_line_word_indexes = [i]
        # last line
        last_line = ""
        for i in cur_line_word_indexes:
            last_line += words[i]
            if len(last_line) < maxWidth:
                last_line += ' '
        if len(last_line) < maxWidth:
            last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(Solution().fullJustify(words, maxWidth))