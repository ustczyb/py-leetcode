# # 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。 
# # 
# # 
# # 字符 数值
# # I 1
# # V 5
# # X 10
# # L 50
# # C 100
# # D 500
# # M 1000 
# # 
# # 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + 
# 
# # II 。 
# # 
# # 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 
# 5
# # 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况： 
# # 
# # 
# # I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 
# # X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# # C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 
# # 
# # 
# # 给你一个整数，将其转为罗马数字。 
# # 
# # 
# # 
# # 示例 1: 
# # 
# # 
# # 输入: num = 3
# # 输出: "III" 
# # 
# # 示例 2: 
# # 
# # 
# # 输入: num = 4
# # 输出: "IV" 
# # 
# # 示例 3: 
# # 
# # 
# # 输入: num = 9
# # 输出: "IX" 
# # 
# # 示例 4: 
# # 
# # 
# # 输入: num = 58
# # 输出: "LVIII"
# # 解释: L = 50, V = 5, III = 3.
# # 
# # 
# # 示例 5: 
# # 
# # 
# # 输入: num = 1994
# # 输出: "MCMXCIV"
# # 解释: M = 1000, CM = 900, XC = 90, IV = 4. 
# # 
# # 
# # 
# # 提示： 
# # 
# # 
# # 1 <= num <= 3999 
# # 
# # Related Topics 哈希表 数学 字符串 👍 861 👎 0
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = ''
        thousand_nums = int(num / 1000)
        for i in range(thousand_nums):
            res += 'M'
        hundrund_nums = int((num - thousand_nums * 1000) / 100)
        if hundrund_nums > 8:
            res += 'C' * (10 - hundrund_nums) + 'M'
        elif hundrund_nums >= 5:
            res += 'D' + 'C' * (hundrund_nums - 5)
        elif hundrund_nums > 3:
            res += 'C' * (5 - hundrund_nums) + 'D'
        else:
            res += 'C' * hundrund_nums
        ten_nums = int((num % 100) / 10)
        if ten_nums > 8:
            res += 'X' * (10 - ten_nums) + 'C'
        elif ten_nums >= 5:
            res += 'L' + 'X' * (ten_nums - 5)
        elif ten_nums > 3:
            res += 'X' * (5 - ten_nums) + 'L'
        else:
            res += 'X' * ten_nums
        one_nums = num % 10
        if one_nums > 8:
            res += 'I' * (10 - one_nums) + 'X'
        elif one_nums >= 5:
            res += 'V' + 'I' * (one_nums - 5)
        elif one_nums > 3:
            res += 'I' * (5 - one_nums) + 'V'
        else:
            res += 'I' * one_nums
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().intToRoman(4))