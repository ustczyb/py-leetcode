# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  示例 1: 
# 
#  输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  说明： 
# 
#  
#  num1 和 num2 的长度小于110。 
#  num1 和 num2 只包含数字 0-9。 
#  num1 和 num2 均不以零开头，除非是数字 0 本身。 
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。 
#  
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        c = 0
        res = ''
        l1 = len(num1)
        l2 = len(num2)
        for i in range(l1 + l2):
            tmp = 0
            j = max(0, i - l2 + 1)
            while j <= i and j < l1:
                k = i - j
                tmp += int(num1[l1 - 1 - j]) * int(num2[l2 - 1 - k])
                j += 1
            tmp += c
            c = int(tmp / 10)
            res = str(tmp % 10) + res
        if res[0] == '0':
            return res[1:]
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().multiply('123', '456'))
