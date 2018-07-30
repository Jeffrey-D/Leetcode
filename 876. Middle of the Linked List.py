# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = []
        
        while head != None:
            list.append(head.val)
            # p = p.next
            head = head.next
        
        if len(list) % 2 == 0:
            return list[len(list)/2 + 1: ]
        else:
            return list[(len(list)+1) / 2 : ]
        
S
