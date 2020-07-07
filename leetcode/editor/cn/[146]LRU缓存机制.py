# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在
# 写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
# 
#  
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self._max_capacity_ = capacity
        self._cur_capacity_ = 0
        self._dict_ = {}
        self._head_ = ListNode()
        self._tail_ = ListNode()
        self._head_.next = self._tail_
        self._tail_.prev = self._head_

    def move_node_to_tail(self, key):
        node = self._dict_[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self._tail_.prev.next = node
        node.prev = self._tail_.prev
        node.next = self._tail_
        self._tail_.prev = node

    def get(self, key: int) -> int:
        if key in self._dict_:
            self.move_node_to_tail(key)
            return self._dict_[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dict_:
            node = self._dict_[key]
            node.value = value
            self.move_node_to_tail(key)
            return
        if self._cur_capacity_ == self._max_capacity_:
            first = self._head_.next
            self._dict_.pop(first.key)
            self._head_.next = first.next
            first.next.prev = self._head_
            self._cur_capacity_ -= 1
        node = ListNode(key, value)
        self._tail_.prev.next = node
        node.prev = self._tail_.prev
        node.next = self._tail_
        self._tail_.prev = node
        self._dict_[key] = node
        self._cur_capacity_ += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))
