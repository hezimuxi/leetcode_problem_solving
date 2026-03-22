#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def add(self, key: int) -> None:
        self.set.add(key)

    def remove(self, key: int) -> None:
        self.set.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.set
    
#无视题目要求嘻嘻嘻嘻嘻嘻


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

