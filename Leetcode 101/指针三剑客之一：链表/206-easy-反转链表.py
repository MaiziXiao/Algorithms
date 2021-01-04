# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        反转一个单链表。

        示例:

        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
        """
        # Time: O(n) Space: O(1)
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return last
