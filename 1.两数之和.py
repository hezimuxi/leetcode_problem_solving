# @lc app=leetcode.cn id=1 lang=python3
# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,v in enumerate(nums):
            prevV = target - v
            if prevV in dict:
                return [dict[prevV], i]
            dict[v] = i
        return []
    
# @lc code=end
           
                