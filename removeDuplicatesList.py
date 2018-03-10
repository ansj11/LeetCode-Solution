# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = head
        p = head.next
        while p:
            if p.val == temp.val:
                temp.next = p.next
                p = p.next
            else:
                temp = p
                p = p.next
        
        return head