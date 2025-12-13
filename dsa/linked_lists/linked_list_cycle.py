"""
Linked List Cycle - LeetCode #141
Frequency: 85% (Extremely common)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

Time Complexity: O(n)
Space Complexity: O(1) with Floyd's algorithm
"""

from typing import Optional
from .list_node import ListNode


def has_cycle_hash_set(head: Optional[ListNode]) -> bool:
    """
    Hash set approach: O(n) space
    """
    visited = set()
    current = head
    
    while current:
        if id(current) in visited:
            return True
        visited.add(id(current))
        current = current.next
    
    return False


def has_cycle_floyd(head: Optional[ListNode]) -> bool:
    """
    Floyd's Cycle Detection (Tortoise and Hare): O(1) space
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Linked List Cycle II - LeetCode #142
    Return the node where the cycle begins, or None if no cycle
    """
    if not head or not head.next:
        return None
    
    # Step 1: Find meeting point
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Step 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# Test cases
if __name__ == "__main__":
    # Create list with cycle
    head1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle: 4 -> 2
    
    print(f"Has cycle: {has_cycle_floyd(head1)}")  # True
    cycle_start = detect_cycle_start(head1)
    print(f"Cycle starts at node with value: {cycle_start.val if cycle_start else None}")
    
    # Create list without cycle
    head2 = ListNode.from_list([1, 2, 3, 4])
    print(f"\nHas cycle: {has_cycle_floyd(head2)}")  # False

