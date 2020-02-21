# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

    Example 1:
    Input: 1->2->3->4->5->5
    Output: 1->2->5

    Example 2:
    Input: 1->1->1->2->3
    Output: 2->3
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        这里先用一个tmp临时存储上一个元素，然后当遍历到下一个待插入元素时，
        把待插入元素和tmp以及待插入元素的下个元素都比较一下，只有都不相等，才能插入。
        """
        if head == None or head.next == None:
            return head
        new_head = ListNode(None)
        tmp = None
        r = new_head
        while head:
            next = head.next
            if (next == None and head.val != tmp) or (next != None and head.val!=tmp and head.val !=next.val):
                r.next = head
                r = head
                # 万一最后一个节点会变None
                r.next = None
            tmp = head.val
            head = next

        return new_head.next

#[1,2,3,3,4,4,5]