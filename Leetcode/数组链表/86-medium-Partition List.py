# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.

    Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Solution 1: 两个新链表
        # 设定两个虚拟节点，dummyHead1用来保存小于该值的链表，dummyHead2来保存大于等于该值的链表
        # 遍历整个原始链表，将小于该值的放于dummyHead1中，其余的放置在dummyHead2中
        # 遍历结束后，将dummyHead2插入到dummyHead1后面
        dummy_1 = dummy_1_head = ListNode(None)
        dummy_2 = dummy_2_head = ListNode(None)
        curr_node = head
        while curr_node:
            if curr_node.val < x:
                dummy_1.next = ListNode(curr_node.val)
                dummy_1 = dummy_1.next
            else:
                dummy_2.next = ListNode(curr_node.val)
                dummy_2 = dummy_2.next
            curr_node = curr_node.next
        dummy_1.next = dummy_2_head.next
        return dummy_1_head.next

        # Solution 2: In place Solution
        first_node = ListNode(0)
        first_node.next = head
        # 设计三个指针
        # 一个指向小于x的最后一个节点，即前后分离点
        # 一个指向当前遍历节点的前一个节点
        # 一个指向当前遍历的节点
        sep_node = first_node
        pre_node = first_node
        current_node = head

        while current_node is not None:
            if current_node.val < x:
                # 注意有可能出现前一个节点就是分离节点的情况
                if pre_node is sep_node:
                    pre_node = current_node
                    sep_node = current_node
                    current_node = current_node.next
                else:
                    # 这段次序比较烧脑
                    pre_node.next = current_node.next
                    current_node.next = sep_node.next
                    sep_node.next = current_node
                    sep_node = current_node
                    current_node = pre_node.next
            else:
                pre_node = current_node
                current_node = pre_node.next

        return first_node.next
