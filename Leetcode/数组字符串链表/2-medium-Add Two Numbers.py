# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    # You are given two linked lists representing two non-negative numbers.
    # The digits are stored in reverse order and each of their nodes contain a single digit.
    # Add the two numbers and return it as a linked list.
    #
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1. own solution
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        p = l1
        q = l2
        while p != None or q != None:
            if p is not None:
                x = p.val
                p = p.next
            else:
                x = 0
            if q is not None:
                y = q.val
                q = q.next
            else:
                y = 0
            sum = x + y + carry
            carry, value = sum // 10, sum % 10
            curr.next = ListNode(value)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

        # 2. online
        # dummy = ListNode(0)
        # # current is the current ListNode and carry is the value
        # current, carry = dummy, 0
        # # when linked list is not till the end
        # while l1 or l2:
        #     val = carry
        #     if l1:
        #         val += l1.val
        #         l1 = l1.next
        #     if l2:
        #         val += l2.val
        #         l2 = l2.next
        #     carry, val = val // 10, val % 10
        #     current.next = ListNode(val)
        #     current = current.next
        # # When l1, l2 same length and there should be an extra ListNode
        # if carry == 1:
        #     current.next = ListNode(1)
        # return dummy.next


a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution().addTwoNumbers(a, b)
print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
