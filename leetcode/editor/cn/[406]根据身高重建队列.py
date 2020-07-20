# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来
# 重建这个队列。 
# 
#  注意： 
# 总人数少于1100人。 
# 
#  示例 
# 
#  
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#  
#  Related Topics 贪心算法

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from functools import cmp_to_key
class Solution:

    def letter_cmp(self, a, b):
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return -1
            else:
                return 1
        else:
            return -1

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=cmp_to_key(self.letter_cmp))
        res = []
        for p in sorted_people:
            if p[1] == 0:
                res.insert(0, p)
            else:
                count = 0
                for i in range(len(res)):
                    if res[i][0] >= p[0]:
                        count += 1
                        if count == p[1]:
                            res.insert(i + 1, p)
                            break
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
