# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        请判断一个链表是否为回文链表。

        示例 1:

        输入: 1->2
        输出: false
        示例 2:

        输入: 1->2->2->1
        输出: true
        """
        # fast = slow = head

        # # find mid point which including (first) mid point into the first half linked list
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # node = None

        # # reverse second half linked list
        # while slow:
        #     slow.next, slow, node = node, slow.next, slow

        # # compare reversed and original half; must maintain reversed linked list is shorter than 1st half
        # while node:
        #     if node.val != head.val:
        #         return False
        #     node = node.next
        #     head = head.next
        # return True

        # 用List
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        N = len(vals)
        left, right = 0, N - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True
