"""
Reverse Linked List - LeetCode #206
Frequency: 90% (Extremely common)

Reverse a singly linked list.

Time Complexity: O(n)
Space Complexity: O(1) iterative, O(n) recursive
"""

from typing import Optional
from .list_node import ListNode


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iterative approach: O(1) space
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Recursive approach: O(n) space (call stack)
    """
    if not head or not head.next:
        return head
    
    # Reverse rest of the list
    reversed_head = reverse_list_recursive(head.next)
    
    # Reverse current node
    head.next.next = head
    head.next = None
    
    return reversed_head


def reverse_list_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse Linked List II - LeetCode #92
    Reverse nodes from position left to position right
    """
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to left position
    for _ in range(left - 1):
        prev = prev.next
    
    # Reverse the sublist
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next


# Test cases
if __name__ == "__main__":
    # Test reverse full list
    head1 = ListNode.from_list([1, 2, 3, 4, 5])
    print(f"Original: {head1}")
    reversed1 = reverse_list_iterative(head1)
    print(f"Reversed: {reversed1}")
    print(f"As list: {reversed1.to_list() if reversed1 else []}")
    
    # Test reverse between positions
    head2 = ListNode.from_list([1, 2, 3, 4, 5])
    print(f"\nOriginal: {head2}")
    reversed2 = reverse_list_between(head2, 2, 4)
    print(f"Reversed between 2-4: {reversed2}")
    print(f"As list: {reversed2.to_list() if reversed2 else []}")

