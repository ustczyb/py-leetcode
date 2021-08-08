# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列： 
# 
#  
#  序列中第一个单词是 beginWord 。 
#  序列中最后一个单词是 endWord 。 
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典 wordList 中的单词。 
#  
# 
#  给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中
# 的 单词数目 。如果不存在这样的转换序列，返回 0。 
#  
# 
#  示例 1： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","lo
# g","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","lo
# g"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= beginWord.length <= 10 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成 
#  beginWord != endWord 
#  wordList 中的所有字符串 互不相同 
#  
#  Related Topics 广度优先搜索 哈希表 字符串 
#  👍 814 👎 0

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

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        source_queue = [beginWord]
        target_queue = [endWord]
        source_visited = {beginWord: 0}
        target_visited = {endWord: 0}
        while source_queue or target_queue:
            if source_queue:
                word = source_queue.pop(0)
                for neighbor in self.findNeighBors(word, wordList):
                    if neighbor in target_visited:
                        return target_visited[neighbor] + source_visited[word] + 2
                    if neighbor not in source_visited:
                        source_queue.append(neighbor)
                        source_visited[neighbor] = source_visited[word] + 1
            if target_queue:
                word = target_queue.pop(0)
                for neighbor in self.findNeighBors(word, wordList):
                    if neighbor in source_visited:
                        return source_visited[neighbor] + target_visited[word] + 2
                    if neighbor not in target_visited:
                        target_queue.append(neighbor)
                        target_visited[neighbor] = target_visited[word] + 1
        return 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    beginWord = "cet"
    endWord = "ism"
    wordList = ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
     "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan",
     "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
     "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry", "led",
     "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
     "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
     "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
     "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag",
     "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
     "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
     "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod",
     "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
     "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and",
     "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
     "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
     "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum",
     "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw",
     "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
     "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex",
     "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
     "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
     "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye",
     "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug",
     "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
     "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
     "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc",
     "moe", "caw", "eel", "dix", "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
     "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
     "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con",
     "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
     "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah", "hie",
     "aim", "ike", "jed", "ego", "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal",
     "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac",
     "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid", "god", "duo", "lin", "aid",
     "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
     "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob", "mow", "jot",
     "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe", "amp", "ale",
     "bud", "gee", "pin", "dun", "pat", "ten", "mob"]
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
