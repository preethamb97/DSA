"""
Remove Nth Node From End of List - LeetCode #19
Frequency: 85% (Extremely common)

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional
from .list_node import ListNode


def remove_nth_from_end(
    head: Optional[ListNode],
    n: int
) -> Optional[ListNode]:
    """
    Two pointers approach
    """
    dummy = ListNode(0)
    dummy.next = head
    
    # Move fast pointer n+1 steps ahead
    fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both pointers until fast reaches end
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove nth node
    slow.next = slow.next.next
    
    return dummy.next


def remove_nth_from_end_two_pass(
    head: Optional[ListNode],
    n: int
) -> Optional[ListNode]:
    """
    Two-pass approach: count length first
    """
    # First pass: count length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Calculate position from start
    position = length - n
    
    # Handle removing head
    if position == 0:
        return head.next
    
    # Second pass: remove node
    current = head
    for _ in range(position - 1):
        current = current.next
    
    current.next = current.next.next
    
    return head


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5], n=2 -> [1,2,3,5]
    head1 = ListNode.from_list([1, 2, 3, 4, 5])
    result1 = remove_nth_from_end(head1, 2)
    print(f"Remove 2nd from end of [1,2,3,4,5]:")
    print(f"Result: {result1.to_list() if result1 else []}")
    print(f"Expected: [1, 2, 3, 5]")
    
    # Test case 2: [1], n=1 -> []
    head2 = ListNode.from_list([1])
    result2 = remove_nth_from_end(head2, 1)
    print(f"\nRemove 1st from end of [1]:")
    print(f"Result: {result2.to_list() if result2 else []}")
    print(f"Expected: []")
    
    # Test case 3: [1,2], n=1 -> [1]
    head3 = ListNode.from_list([1, 2])
    result3 = remove_nth_from_end(head3, 1)
    print(f"\nRemove 1st from end of [1,2]:")
    print(f"Result: {result3.to_list() if result3 else []}")
    print(f"Expected: [1]")

