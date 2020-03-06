# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given a linked list, rotate the list to the right by k places, where k is non-negative.

    Example 1:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

    Example 2
    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # Own solution
        if head == None or head.next == None:
            return head

        current_node = head
        # Count the length of the Linked list
        length_list = 1
        while current_node.next is not None:
            length_list += 1
            current_node = current_node.next
        # current node is the last node, 把链表变成环形链表,等等再找地方断开
        current_node.next = head

        k = k%length_list
        # 重置current node
        current_node = head
        for _ in range(length_list-k-1):
            current_node = current_node.next
        new_head = current_node.next
        current_node.next = None

        return new_head

        # 一次遍历 https://blog.csdn.net/fuxuemingzhu/article/details/80788107
        # if not head or not head.next: return head
        # _len = 0
        # root = head
        # while head:
        #     _len += 1
        #     head = head.next
        # k %= _len
        # if k == 0: return root
        # fast, slow = root, root
        # while k - 1:
        #     fast = fast.next
        #     k -= 1
        # pre = slow
        # while fast.next:
        #     fast = fast.next
        #     pre = slow
        #     slow = slow.next
        # pre.next = None
        # fast.next = root
        # return slow

