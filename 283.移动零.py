class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1          # 列表变短了，总长度-1
                # i 不变，继续检查新挪到 i 位置的元素
            else:
                i += 1

#另外一种解法：
#class Solution:
 #   def moveZeroes(self, nums: List[int]) -> None:
 #       j = 0
 #       for i in range(len(nums)):
 #           if nums[i] != 0:
#              nums[j] = nums[i]
#              j += 1
#      for k in range(j, len(nums)):
#          nums[k] = 0
