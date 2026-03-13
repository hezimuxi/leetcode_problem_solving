#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy
        # while head:
        #     prev.next = head.next
        #     head.next=dummy.next
        #     dummy.next = head
        #     head = prev.next
        # return dummy.next
        # 超时啦！
        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy
        # while head:
        #     dummy.next = head.next
        #     prev = head
        #     head = head.next
        #     prev.next = dummy
        # dummy = None
        # return prev
        #又超时啦，我是唐璧
        #到底怎么做呢
        # dummy = ListNode(0)
        # firstnode = head
        # prev = head
        # head = head.next
        # firstnode.next = None

        # dummy.next = firstnode
        # while head:
        #     dummy.next = head
        #     head = head.next
        #     prev.next = firstnode
        #     prev = head
        # return dummy.next
        #又超时了

        #我决定这道题以后再写






    


        
# @lc code=end

