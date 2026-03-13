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

           
                