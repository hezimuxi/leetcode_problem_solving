#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
#我好菜呜呜呜呜呜呜呜呜呜呜

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{': #不要写成item == '(' or '[' or '{'，这样会导致条件永远为真
                stack.append(item)
            else:
                if not stack: 
                    return False 
                top = stack.pop()
                if (item == ')' and top != '(') or \
                   (item == ']' and top != '[') or \
                   (item == '}' and top != '{'):
                    return False
        return len(stack) == 0

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 右括号映射到左括号，用字典！！！！！！！
        pairs = {')': '(', ']': '[', '}': '{'}
        for item in s:
            if item in pairs:  # 是右括号
                # 栈空或不匹配直接寄
                if not stack or stack[-1] != pairs[item]:
                    return False
                stack.pop()
            else:  # 是左括号
                stack.append(item)
        
        return len(stack) == 0
# @lc code=end

        
# @lc code=end

