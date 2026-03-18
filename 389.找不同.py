#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
#使用哈希表
# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}  
        for char in t:
            count[char] = count.get(char, 0) + 1  
        for char in s:
            count[char] -= 1
            if count[char] == 0:
                del count[char]  
        return list(count.keys())[0]  

#我写的这是什么东西
#下面写的比我好，其实思路差不多。但人家直接用了26个字母的哈希表，感觉更简洁一些。
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s.length == 0:
            return t[0]
        hashtable = [0] * 26
        for i in range(len(s)):
            hashtable[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            hashtable[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if hashtable[i] == -1:
                return chr(i + ord('a'))
# @lc code=end

