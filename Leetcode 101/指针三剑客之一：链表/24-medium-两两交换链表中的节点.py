# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

         

        示例 1：
        输入：head = [1,2,3,4]
        输出：[2,1,4,3]
        """
        dummy_head = last = ListNode()
        dummy_head.next = head
        while head and head.next:
            tmp = head.next.next
            last.next = head.next
            last.next.next = head
            head.next = tmp

            last = head
            head = tmp

        return dummy_head.next


Solution().swapPairs(ListNode(1, ListNode(2)))