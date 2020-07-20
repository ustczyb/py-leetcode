# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
#  Related Topics 栈 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def is_number(self, ch) -> bool:
        if ord(ch) - ord('0') < 10:
            return True
        return False

    def get_type(self, ch) -> int:
        if self.is_number(ch):
            return 1
        if ch == '[' or ch == ']':
            return 2
        return 0

    def decodeString(self, s: str) -> str:
        num_stack = []
        word_stack = ['']
        last_type = 0
        for ch in s:
            type = self.get_type(ch)
            if type == 0:
                word_stack[-1] += ch
            elif type == 1:
                if last_type != 1:
                    num_stack.append(ch)
                else:
                    num_stack[-1] += ch
            else:
                if ch == '[':
                    word_stack.append('')
                else:
                    word = word_stack.pop()
                    num = int(num_stack.pop())
                    tmp = ''
                    for i in range(num):
                        tmp += word
                    word_stack[-1] += tmp
            last_type = type
        return word_stack[-1]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().decodeString("3[a2[c]]"))
    # print(ord('9'))
