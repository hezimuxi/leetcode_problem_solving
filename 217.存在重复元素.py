#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for v in enumerate(nums):
            if v in dict:
                return True
            dict[v] = 1
        return False
#感觉稍微有点多余了的样子......

        
# @lc code=end

#巧妙的解法：

class Solution:                                                              
       def containsDuplicate(self, nums: List[int]) -> bool:                    
             return len(nums) != len(set(nums))  # set会自动去重，如果长度不一样说明有重复元素
# s = set()          # 空集合                                                  
# s = {1, 2, 3}      # 直接创建                                                
# s = set([1, 2, 2, 3])  # 从列表转换 → 自动去重 → {1, 2, 3}               