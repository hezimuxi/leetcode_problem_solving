#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
#使用hashtable和堆
# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if word in dict:
                dict[word]-=1
            else:
                dict[word]=0
        maxheap = []
        for key in dict:
            heapq.heappush(maxheap,(dict[key],key))
            #这里用到元组
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxheap)[1])
            #所以取1就行了
        return res
    

        
# @lc code=end

