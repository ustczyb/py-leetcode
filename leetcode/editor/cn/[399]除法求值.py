# 给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，
# 则返回 -1.0。 
# 
#  示例 : 
# 给定 a / b = 2.0, b / c = 3.0 
# 问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# 返回 [6.0, 0.5, -1.0, 1.0, -1.0 ] 
# 
#  输入为: vector<pair<string, string>> equations, vector<double>& values, vector<p
# air<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.siz
# e()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。 
# 
#  基于上述例子，输入如下： 
# 
#  equations(方程式) = [ ["a", "b"], ["b", "c"] ],
# values(方程式结果) = [2.0, 3.0],
# queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] 
# ]. 
#  
# 
#  输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。 
#  Related Topics 并查集 图

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_dict = {}
        for i in range(len(equations)):
            node_dict[equations[i][0]] = (equations[i][0], 1)
            node_dict[equations[i][1]] = (equations[i][1], 1)

        def find(x):
            if x == node_dict[x][0]:
                return node_dict[x]
            root, sub_val = find(node_dict[x][0])
            node_dict[x] = root, sub_val * node_dict[x][1]
            return node_dict[x]

        def union(a, b, value):
            root_a, val_a = find(a)
            root_b, val_b = find(b)
            if root_a != root_b:
                node_dict[root_a] = (root_b, value * val_b / val_a)
                find(a)


        for i in range(len(equations)):
            union(equations[i][0], equations[i][1], values[i])

        res = []
        for q in queries:
            if q[0] not in node_dict or q[1] not in node_dict:
                res.append(-1.0)
            else:
                root_0, val_0 = find(q[0])
                root_1, val_1 = find(q[1])
                if root_0 == root_1:
                    res.append(val_0 / val_1)
                else:
                    res.append(-1.0)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, queries))
