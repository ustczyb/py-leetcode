"""
给定一副牌 判断是否和牌 (川麻基本牌型 没有风 不考虑七小对 十三幺等特殊牌型 考虑杠)
输入点数按照升序排列
"""
from typing import List, Tuple


def check_one_type(cards: List[int]) -> Tuple[bool, int, int]:
    length = len(cards)
    if length == 0:
        return True, 0, 0
    if length == 1:
        return False, -1, -1
    if length == 2:
        if cards[0] == cards[-1]:
            return True, 1, 0
        else:
            return False, -1, -1
    if length == 3:
        if cards[0] == cards[-1] or (cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2]):
            return True, 0, 1
        else:
            return False, 0, 0
    if length == 4:
        if cards[0] == cards[-1]:
            return True, 0, 1
        else:
            return False, 0, 0
    for i in [2, 3, 4]:
        status, jiang_nums, shunzi_nums = check_one_type(cards[:i])
        if status:
            rest_status, rest_jiang, rest_shunzi = check_one_type(cards[i:])
            if rest_status:
                return True, jiang_nums + rest_jiang, shunzi_nums + rest_shunzi
    return False, -1, -1


def has_win(bings: List[int], tiaos: List[int], wans: List[int]):
    jiang_nums = 0
    shunzi_nums = 0
    for cards in [bings, tiaos, wans]:
        status, sub_jiang, sub_shunzi = check_one_type(cards)
        if not status:
            return False
        jiang_nums += sub_jiang
        shunzi_nums += sub_shunzi
    return jiang_nums == 1 and shunzi_nums == 4


if __name__ == '__main__':
    bings = []
    wans = [1, 1, 1, 1, 2, 3, 4, 5, 6]
    tiaos = [4, 5, 6, 7, 7]
    print(has_win(bings, tiaos, wans))