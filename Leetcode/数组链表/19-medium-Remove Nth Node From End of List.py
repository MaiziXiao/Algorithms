# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:
    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.
    Follow up:
    Could you do this in one pass?
    """
    def removeNthFromEnd(self, head, n):
        """
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        # dummy is important when removing the head (corner case)
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy
        len_list = 0
        node_list = [dummy]
        while current_node.next is not None:
            len_list += 1
            current_node = current_node.next
            node_list.append(current_node)
        node_before = node_list[len_list-n]
        if n == 1:
            node_before.next = None
        else:
            node_after = node_list[len_list-n+2]
            node_before.next = node_after
        return dummy.next

a, a.next, a.next.next, a.next.next.next, a.next.next.next.next = \
    ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
result = Solution().removeNthFromEnd(a, 2)
print("{0} -> {1} -> {2} -> {3}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val))