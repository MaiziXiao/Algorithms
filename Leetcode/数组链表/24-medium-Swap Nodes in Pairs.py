# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Given a linked list, swap every two adjacent nodes and return its head.
        You may not modify the values in the list's nodes, only nodes itself may be changed.

        Example:
        Given 1->2->3->4, you should return the list as 2->1->4->3.
        """
        dummy = curr = ListNode(0)
        dummy.next = head
        # when current nodes have two next nodes
        while curr.next and curr.next.next:
            tmp = curr.next
            tmp_2 = curr.next.next.next
            curr.next = curr.next.next
            curr.next.next = tmp
            curr.next.next.next = tmp_2
            curr = curr.next.next
        return dummy.next

b, b.next, b.next.next, b.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
result = Solution().swapPairs(b)
print("{0} -> {1} -> {2} -> {3}".format(result.val, result.next.val, result.next.next.val,
                                                      result.next.next.next.val))