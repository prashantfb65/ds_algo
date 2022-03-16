"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

E.g.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    current = head
    counter = 0
    while current:
        current = current.next
        counter+=1
    if n == counter:
        return head.next
    r = counter - n -1
    current = head
    while r>0:
        current = current.next
        r-=1
    current.next = current.next.next
    return head