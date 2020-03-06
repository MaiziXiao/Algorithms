# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Reverse a linked list from position m to n. Do it in one-pass.

    Note: 1 ≤ m ≤ n ≤ length of list.

    Example:

    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head
        i = 1
        last_node_before_break = dummy_head
        last_node_to_reverse = None
        last_node = dummy_head
        while head and i <= n:
            print(i, head.val)
            if i + 1 == m:
                last_node_before_break = head
            if m <= i <= n:
                curr_node = ListNode(head.val)
                curr_node.next = last_node
                last_node = curr_node
                if m == i:
                    last_node_to_reverse = curr_node
            i += 1
            head = head.next
        last_node_before_break.next = curr_node
        last_node_to_reverse.next = head

        return dummy_head.next

b, b.next, = ListNode(3), ListNode(5)
result = Solution().reverseBetween(b, 1, 2)
print("{0} -> {1} ".format(result.val, result.next.val))