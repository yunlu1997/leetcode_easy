"""
 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = res  # 指针指向结果链表
            res = cur       # 进行局部交换
            cur = temp      # 右移cur
        return res
