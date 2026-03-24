#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next or not head.next.next:
            return False
        f=head.next
        q=head.next.next
        while(f!=q):
            if not q or not q.next or not f or not f.next:
                return False
            f=f.next
            q=q.next.next
        return True
#另外一种写法:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# @lc code=end

