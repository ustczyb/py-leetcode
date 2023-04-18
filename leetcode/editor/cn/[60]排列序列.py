# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。 
# 
#  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下： 
# 
#  
#  "123" 
#  "132" 
#  "213" 
#  "231" 
#  "312" 
#  "321" 
#  
# 
#  给定 n 和 k，返回第 k 个排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, k = 3
# 输出："213"
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 4, k = 9
# 输出："2314"
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3, k = 1
# 输出："123"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  1 <= k <= n! 
#  
#  Related Topics 数学 回溯算法 
#  👍 538 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # 计算n!
        n_plus = 1
        for i in range(1, n):
            n_plus *= i

        res = ""
        s = int((k - 1) / n_plus)
        left = (k - 1) % n_plus
        res += str(s + 1)
        if left == 0:
            for i in range(1, n + 1):
                if i != s + 1:
                    res += str(i)
        else:
            sub_res = self.getPermutation(n - 1, left + 1)
            for ch in sub_res:
                if int(ch) < s + 1:
                    res += ch
                else:
                    res += str(int(ch) + 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().getPermutation(3, 1))
