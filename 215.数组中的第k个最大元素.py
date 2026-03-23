#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        minheap = []
        for num in nums:
            heapq.heappush(minheap,num)
        while(len(minheap)>k):
            heapq.heappop(minheap)
        return minheap[0]

# @lc code=end
#堆真好用

