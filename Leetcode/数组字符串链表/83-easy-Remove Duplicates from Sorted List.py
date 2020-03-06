# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    Example 1:
    Input: 1->1->2
    Output: 1->2
    Example 2:

    Input: 1->1->2->3->3
    Output: 1->2->3
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        curr_node = head
        last_node = dummy
        while curr_node:
            if last_node.val != curr_node.val:
                last_node.next = curr_node
                last_node = curr_node
            # curr_node是最后一个node的时候,要特殊情况
            if curr_node.next is None and last_node.val == curr_node.val:
                last_node.next = None
            curr_node = curr_node.next
        return dummy.next

# [1,1,2,3,3]