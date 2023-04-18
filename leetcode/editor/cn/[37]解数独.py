# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  数独的解法需 遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  
# 
#  
#  
#  
#  示例： 
# 
#  
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5","."
# ,".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".","."
# ,"3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"
# ],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],["
# .",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"
# ],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["
# 4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","
# 6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","
# 5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
# 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字或者 '.' 
#  题目数据 保证 输入数独仅有一个解 
#  
#  
#  
#  
#  Related Topics 哈希表 回溯算法 
#  👍 821 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def locate_square_index(row, col):
            return int(row / 3) * 3 + int(col / 3)

        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        square_dict = defaultdict(set)
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                ch = board[i][j]
                if ch != '.':
                    row_dict[i].add(ch)
                    col_dict[j].add(ch)
                    square_dict[locate_square_index(i, j)].add(ch)

        def check(row, col, value):
            # 在(row, col)处填入value是否满足条件
            # 判断同一行是否有重复
            if value in row_dict[row]:
                return False
            # 同一列是否有重复
            if value in col_dict[col]:
                return False
            # 同一宫格是否有重复
            if value in square_dict[locate_square_index(row, col)]:
                return False
            return True

        def set_value(row, col):
            if board[row][col] != '.':
                # already set
                if col == 8:
                    if row < 8:
                        return set_value(row + 1, 0)
                    else:
                        return board
                else:
                    return set_value(row, col + 1)
            else:
                for i in range(1, 10):
                    i = str(i)
                    if check(row, col, i):
                        board[row][col] = i
                        row_dict[row].add(i)
                        col_dict[col].add(i)
                        square_dict[locate_square_index(row, col)].add(i)
                        if col == 8:
                            if row < 8:
                                sub_res = set_value(row + 1, 0)
                                if sub_res != -1:
                                    return sub_res
                            else:
                                return board
                        else:
                            sub_res = set_value(row, col + 1)
                            if sub_res != -1:
                                return sub_res
                        board[row][col] = '.'
                        row_dict[row].remove(i)
                        col_dict[col].remove(i)
                        square_dict[locate_square_index(row, col)].remove(i)
                return -1
        return set_value(0, 0)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board))
