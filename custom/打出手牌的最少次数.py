"""
从一副去掉大小王的扑克牌(52张)中 随机选择17张发到玩家的手上 出牌规则如下：
1. 可以一次出任意一张牌
2. 可以一次出x张点数相同的牌和任意(x-2)个单牌或者对子, 也可以不带  (对子, 3带1, 3带1对, 4带2, 4带2对)
3. 可以一次出x张点数连续的牌(x>=5) 连续指3-A的子序列 3,4,5,6,7是连续的 10,11,12,13,1是连续的 但2,3,4,5,6不是连续的
问打出所有手牌至少需要多少次？

可以先考虑前两种出牌方式 再考虑添加第三种出牌方式 甚至加入连对，飞机等规则
如果我们要对手牌打分 可以怎样设计 (开放式)？

搜索, BFS
"""

from typing import List
from collections import defaultdict

def remove_series(cards: List[int], start: int, end: int):
    for i in range(start, end + 1):
        cards[i] -= 1
    return cards

def min_times(cards: List[int]) -> int:

    # find series
    lack_numbers = [0]
    for i in range(1, 13):
        if cards[i] == 0:
            lack_numbers.append(i)
    lack_numbers.append(13)
    min_times_with_series = 17
    for j in range(len(lack_numbers) - 1):
        if lack_numbers[j + 1] - lack_numbers[j] > 5:
            for start in range(lack_numbers[j] + 1, lack_numbers[j + 1] - 4):
                for end in range(start + 4, lack_numbers[j + 1]):
                    new_cards = remove_series(cards[:], start, end)
                    min_times_with_series = min(min_times_with_series, min_times(new_cards) + 1)

    # if no series
    count_dict = defaultdict(int)
    for i in range(13):
        count_dict[cards[i]] += 1

    res = 0

    res += count_dict[4]
    if count_dict[1] >= 2 * count_dict[4]:
        count_dict[1] -= count_dict[4] * 2
    else:
        four_with_one_count = int(count_dict[1] / 2)
        count_dict[1] -= four_with_one_count * 2
        count_dict[4] -= four_with_one_count
        if count_dict[2] >= 2 * count_dict[4]:
            count_dict[2] -= 2 * count_dict[4]
        else:
            four_with_couple_count = int(count_dict[2] / 2)
            count_dict[2] -= four_with_couple_count * 2


    res += count_dict[3]
    if count_dict[1] >= count_dict[3]:
        count_dict[1] -= count_dict[3]
    else:
        if count_dict[2] >= count_dict[3] - count_dict[1]:
            count_dict[2] -= count_dict[3] - count_dict[1]
        else:
            count_dict[2] = 0
        count_dict[1] = 0

    res += count_dict[2]
    res += count_dict[1]
    return min(res, min_times_with_series)


if __name__ == '__main__':
    # cards = [3, 1, 1, 1, 1, 2, 3, 0, 1, 1, 1, 1, 1]
    cards = [3, 0, 0, 0, 0, 1, 3, 1, 2, 2, 2, 2, 1]
    print(min_times(cards))