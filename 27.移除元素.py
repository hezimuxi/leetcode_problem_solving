#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i] ==val:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        
        return n

        
# @lc code=end

