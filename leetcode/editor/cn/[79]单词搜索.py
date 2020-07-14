# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        visited_row = [False] * len(board[0])
        visited = []
        for i in range(len(board)):
            visited.append(visited_row.copy())
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, visited, i, j, word):
                    return True
        return False

    def search(self, board: List[List[str]], visited: List[List[bool]], row: int, col: int, word: str) -> bool:
        if not word:
            return True
        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
            return False
        if board[row][col] != word[0] or visited[row][col]:
            return False
        visited[row][col] = True
        res = self.search(board, visited, row + 1, col, word[1:]) or \
              self.search(board, visited, row - 1, col, word[1:]) or \
              self.search(board, visited, row, col + 1, word[1:]) or \
              self.search(board, visited, row, col - 1, word[1:])
        visited[row][col] = False
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    board = [["a", "a"], ["a", "a"], ["a", "a"]]
    print(Solution().exist(board, 'aaaaaaa'))
