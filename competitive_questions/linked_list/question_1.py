"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

from typing import Optional


class Node:

    def __init__(self, element) -> None:
        self.element = element
        self.next = None

class Solution:

    def middle_element_ap1(self, head: Optional[Node]) -> Optional[Node]:
        counter = 0
        temp_head = head
        while head:
            head = head.next
            counter+=1
        n = counter//2
        while n>0:
            temp_head = temp_head.next
            n-=1
        return temp_head

    def middle_element_ap2(self, head: Optional[Node]) -> Optional[Node]:
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    sol = Solution()
    # print(sol.middle_element(ll))

