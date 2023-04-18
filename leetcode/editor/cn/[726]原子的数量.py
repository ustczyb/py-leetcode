# 给你一个字符串化学式 formula ，返回 每种原子的数量 。 
# 
#  原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。 
# 
#  如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。 
# 
#  
#  例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。 
#  
# 
#  两个化学式连在一起可以构成新的化学式。 
# 
#  
#  例如 "H2O2He3Mg4" 也是化学式。 
#  
# 
#  由括号括起的化学式并佐以数字（可选择性添加）也是化学式。 
# 
#  
#  例如 "(H2O2)" 和 "(H2O2)3" 是化学式。 
#  
# 
#  返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于
#  1），以此类推。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：formula = "H2O"
# 输出："H2O"
# 解释：原子的数量是 {'H': 2, 'O': 1}。
#  
# 
#  示例 2： 
# 
#  
# 输入：formula = "Mg(OH)2"
# 输出："H2MgO2"
# 解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#  
# 
#  示例 3： 
# 
#  
# 输入：formula = "K4(ON(SO3)2)2"
# 输出："K4N2O14S4"
# 解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#  
# 
#  示例 4： 
# 
#  
# 输入：formula = "Be32"
# 输出："Be32"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= formula.length <= 1000 
#  formula 由英文字母、数字、'(' 和 ')' 组成 
#  formula 总是有效的化学式 
#  输出的所有值总是在 32-bit 整数范围内 
#  
#  Related Topics 栈 哈希表 字符串 
#  👍 214 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:

    def count_elements(self, s: str) -> dict:
        cur_element = ''
        count_dict = defaultdict(int)
        length = len(s)
        cur_count = 0
        left_count = 0
        for i in range(length):
            if s[i].isupper():
                if left_count == 0:  # 是否在括号内
                    if cur_element:
                        if cur_count == 0:
                            count_dict[cur_element] += 1
                        else:
                            count_dict[cur_element] += cur_count
                            cur_count = 0
                    cur_element = s[i]
                else:
                    cur_element += s[i]
            elif s[i] == '(':
                if left_count == 0:  # 是否在括号内
                    if cur_element:
                        if cur_count == 0:
                            count_dict[cur_element] += 1
                        else:
                            count_dict[cur_element] += cur_count
                            cur_count = 0
                    cur_element = s[i]
                else:
                    cur_element += s[i]
                left_count += 1
            elif s[i] == ')':
                cur_element += s[i]
                left_count -= 1
            elif s[i].isdigit():
                if left_count == 0:
                    if cur_element:
                        cur_count = cur_count * 10 + int(s[i])
                else:
                    cur_element += s[i]
            else:
                cur_element += s[i]
        count_dict[cur_element] += cur_count if cur_count > 0 else 1

        res_dict = defaultdict(int)

        for element in count_dict:
            if element[0] == '(':
                sub_count = count_dict[element]
                sub_dict = self.count_elements(element[1:-1])
                for k in sub_dict:
                    res_dict[k] += sub_dict[k] * sub_count
                # count_dict.pop(element)
            else:
                res_dict[element] += count_dict[element]
        return res_dict

    def countOfAtoms(self, formula: str) -> str:
        count_dict = self.count_elements(formula)
        res_str = ""
        for k in sorted(count_dict):
            if count_dict[k] > 1:
                res_str += '%s%d' % (k, count_dict[k])
            else:
                res_str += k
        return res_str


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "((B10B23)26(BB46)25B33B15B23(B50)8)3"
    print(Solution().countOfAtoms(s))
