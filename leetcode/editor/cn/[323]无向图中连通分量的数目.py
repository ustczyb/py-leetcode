# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。 
# 
#  示例 1: 
# 
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
# 
#      0          3
#      |          |
#      1 --- 2    4 
# 
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
#      0           4
#      |           |
#      1 --- 2 --- 3
# 
# 输出:  1
#  
# 
#  注意: 
# 你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0] 相同，所以它们不会同时在 edges 中出现。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 
#  👍 93 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = list(range(n))
        self.cnt = n

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if root_p != root_q:
                root[root_p] = root_q
                self.cnt -= 1

        def find(p) -> int:
            if p != root[p]:
                root[p] = find(root[p])
            return root[p]

        for edge in edges:
            union(edge[0], edge[1])
        return self.cnt
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(Solution().countComponents(n, edges))