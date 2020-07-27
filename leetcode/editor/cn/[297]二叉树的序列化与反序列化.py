# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。 
# 
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树 设计

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        def first_travel(root, level=0):
            if not root:
                return []
            res = ['%d_%d' % (root.val, level)]
            res.extend(first_travel(root.left, level + 1))
            res.extend(first_travel(root.right, level + 1))
            return res

        def mid_travel(root, level=0):
            if not root:
                return []
            res = []
            res.extend(mid_travel(root.left, level + 1))
            res.append('%d_%d' % (root.val, level))
            res.extend(mid_travel(root.right, level + 1))
            return res

        return ','.join(first_travel(root)) + '\n' + ','.join(mid_travel(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def build_tree(first_travel, mid_travel):
            if not first_travel:
                return None
            root_val = int(first_travel[0].split('_')[0])
            root = TreeNode(root_val)
            for i in range(len(mid_travel)):
                if mid_travel[i] == first_travel[0]:
                    break
            root.left = build_tree(first_travel[1: i + 1], mid_travel[:i])
            root.right = build_tree(first_travel[i + 1:], mid_travel[i + 1:])
            return root
        if not data:
            return None
        split_arr = data.split('\n')
        first_travel_list = split_arr[0].split(',')
        mid_travel_list = split_arr[1].split(',')
        return build_tree(first_travel_list, mid_travel_list)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    codec = Codec()
    tree = codec.deserialize('3_0,2_1,3_2,4_1\n3_2,2_1,3_0,4_1')
    tree_str = codec.serialize(tree)
    print(tree_str)
