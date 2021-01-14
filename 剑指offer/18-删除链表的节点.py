# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """
        给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

        返回删除后的链表的头节点。

        注意：此题对比原题有改动

        示例 1:
        输入: head = [4,5,1,9], val = 5
        输出: [4,1,9]
        解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

        示例 2:
        输入: head = [4,5,1,9], val = 1
        输出: [4,5,9]
        解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
        """
        dummy_node = ListNode(None)
        dummy_node.next = head
        last_node = dummy_node
        while head:
            if head.val == val:
                last_node.next = head.next
            last_node = head
            head = head.next

        return dummy_node.next


class Solution:
    def deleteDuplication(self, pHead):
        "删除重复的链表节点”
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        # 如果不一样就继续
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                # 当cur.val = cur.next.val的时候，一直找cur.next.next...直到和cur.val不一样
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                # 再把last重置为现在的curr
                last.next = curr
        return first.next