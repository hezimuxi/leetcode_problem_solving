#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       #爷就不用栈。你能把我怎么样
        num=[]
        for item in nums1:
            i=0
            while (nums2[i]!=item and i<len(nums2)):
               i+=1
             # 从 i+1 开始找下一个更大的
            found = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > item:
                    found = nums2[j]
                    break   
            num.append(found)
        return num
       
# @lc code=end

#哈希表
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i,v in enumerate(nums2):
            dict[i] = v
        



       