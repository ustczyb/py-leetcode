# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s
# 1 -> s2 -> ... -> sk 这样的单词序列，并满足： 
# 
#  
#  
#  
#  每对相邻的单词之间仅有单个字母不同。 
#  转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单
# 词。 
#  sk == endWord 
#  
# 
#  给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的
#  最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","lo
# g","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#  
# 
#  示例 2： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","lo
# g"]
# 输出：[]
# 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= beginWord.length <= 7 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成 
#  beginWord != endWord 
#  wordList 中的所有单词 互不相同 
#  
#  
#  
#  Related Topics 广度优先搜索 哈希表 字符串 回溯 
#  👍 456 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isNeighbors(self, word1, word2):
        if len(word1) != len(word2):
            return False
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
                if count > 1:
                    return False
        return count == 1

    def findNeighBors(self, word: str, wordList: List[str]):
        return [w for w in wordList if self.isNeighbors(word, w)]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        if beginWord == endWord:
            return res
        if endWord not in wordList:
            return res
        source_queue = [beginWord]
        target_queue = [endWord]
        source_visited = {beginWord: beginWord}
        target_visited = {endWord: endWord}
        while source_queue or target_queue:
            source_queue_len = len(source_queue)
            for _ in range(source_queue_len):
                word = source_queue.pop(0)
                for neighbor in self.findNeighBors(word, wordList):
                    if neighbor in target_visited:
                        p = word
                        sub_res = []
                        while p != source_visited[p]:
                            sub_res.insert(0, p)
                            p = source_visited[p]
                        sub_res.insert(0, p)
                        p = neighbor
                        while p != target_visited[p]:
                            sub_res.append(p)
                            p = target_visited[p]
                        sub_res.append(p)
                        res.append(sub_res)
                    if neighbor not in source_visited:
                        source_queue.append(neighbor)
                        source_visited[neighbor] = word
            if res:
                return res
            target_queue_len = len(target_queue)
            for _ in range(target_queue_len):
                word = target_queue.pop(0)
                for neighbor in self.findNeighBors(word, wordList):
                    if neighbor in source_visited:
                        p = neighbor
                        sub_res = []
                        while p != source_visited[p]:
                            sub_res.insert(0, p)
                            p = source_visited[p]
                        sub_res.insert(0, p)
                        p = word
                        while p != target_visited[p]:
                            sub_res.append(p)
                            p = target_visited[p]
                        sub_res.append(p)
                        res.append(sub_res)
                    if neighbor not in target_visited:
                        target_queue.append(neighbor)
                        target_visited[neighbor] = word
            if res:
                return res
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().findLadders(beginWord, endWord, wordList))