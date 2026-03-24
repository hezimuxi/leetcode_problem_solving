#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat_num=0
        left = 0
        right = len(people)-1
        people.sort() 
        while(left<right):
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            boat_num+=1
        if left==right:
            boat_num+=1
        return boat_num
    
        
# @lc code=end
