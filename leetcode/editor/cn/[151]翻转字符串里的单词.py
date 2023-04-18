# 给定一个字符串，逐个翻转字符串中的每个单词。 
# 
#  说明： 
# 
#  
#  无空格字符构成一个 单词 。 
#  输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。 
#  如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入："the sky is blue"
# 输出："blue is sky the"
#  
# 
#  示例 2： 
# 
#  输入："  hello world!  "
# 输出："world! hello"
# 解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#  
# 
#  示例 3： 
# 
#  输入："a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
# 
#  示例 4： 
# 
#  输入：s = "  Bob    Loves  Alice   "
# 输出："Alice Loves Bob"
#  
# 
#  示例 5： 
# 
#  输入：s = "Alice does not even like bob"
# 输出："bob like even not does Alice"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 包含英文大小写字母、数字和空格 ' ' 
#  s 中 至少存在一个 单词 
#  
# 
#  
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请尝试使用 O(1) 额外空间复杂度的原地解法。 
#  
#  Related Topics 字符串 
#  👍 313 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_arr = list(s)
        def swap(i, j):
            s_arr[i], s_arr[j] = s_arr[j], s_arr[i]

        # strip blank
        cur_index = 0
        last_word_index = -10
        for i in range(len(s_arr)):
            if s_arr[i] == ' ':
                if last_word_index == i - 1:
                    swap(i, cur_index)
                    cur_index += 1
            else:
                swap(i, cur_index)
                cur_index += 1
                last_word_index = i
        if s_arr[cur_index - 1] != ' ':
            s_arr = s_arr[:cur_index]
        else:
            s_arr = s_arr[:cur_index - 1]
        # reverse all
        s_arr = s_arr[::-1]
        # reverse each word
        last_blank_index = -1
        for i in range(len(s_arr)):
            if s_arr[i] == ' ':
                for j in range(int((i - last_blank_index) / 2)):
                    swap(last_blank_index + 1 + j, i - 1 - j)
                last_blank_index = i
        i = len(s_arr)
        for j in range(int((i - last_blank_index) / 2)):
            swap(last_blank_index + 1 + j, i - 1 - j)
        return ''.join(s_arr)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "  Bob    Loves  Alice   "
    print(Solution().reverseWords(s))