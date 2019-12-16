# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
        nodes of the first two lists.

        Example:
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
        # Own Solution (Iteratively)
        # dummy = ListNode(0)
        # curr = dummy
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         print(l1.val)
        #         curr.next = l1
        #         l1 = l1.next
        #     else:
        #         print(l2.val)
        #         curr.next = l2
        #         l2 = l2.next
        #     curr = curr.next
        # # When it is the last Node, while loop will break so we have to add one remaining Node
        # curr.next = l1 or l2
        # return dummy.next

        # Online Solution (recursively)　动态规划
        def mergeTwoLists(self, l1, l2):
            # 当l1或者l2是空的，返回那个不空的
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

a, a.next, a.next.next = ListNode(1), ListNode(2), ListNode(4)
b, b.next, b.next.next = ListNode(1), ListNode(3), ListNode(4)
result = Solution().mergeTwoLists(a, b)
print("{0} -> {1} -> {2} -> {3} -> {4} -> {5}".format(result.val, result.next.val, result.next.next.val,
                                                      result.next.next.next.val, result.next.next.next.next.val,
                                                      result.next.next.next.next.next.val))