"""
Add Two Numbers - LeetCode #2
Frequency: 95% (Universal question)

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))
"""

from typing import Optional
from .list_node import ListNode


def add_two_numbers(
    l1: Optional[ListNode],
    l2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Iterative approach with carry
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


def add_two_numbers_recursive(
    l1: Optional[ListNode],
    l2: Optional[ListNode],
    carry: int = 0
) -> Optional[ListNode]:
    """
    Recursive approach
    """
    if not l1 and not l2 and carry == 0:
        return None
    
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    total = val1 + val2 + carry
    digit = total % 10
    new_carry = total // 10
    
    node = ListNode(digit)
    node.next = add_two_numbers_recursive(
        l1.next if l1 else None,
        l2.next if l2 else None,
        new_carry
    )
    
    return node


# Test cases
if __name__ == "__main__":
    # Example: 342 + 465 = 807
    # Represented as: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    
    result = add_two_numbers(l1, l2)
    print(f"Input: {l1.to_list()} + {l2.to_list()}")
    print(f"Output: {result.to_list() if result else []}")
    print(f"Expected: [7, 0, 8]")
    
    # Example: 999 + 99 = 1098
    # Represented as: [9,9,9] + [9,9] = [8,9,0,1]
    l3 = ListNode.from_list([9, 9, 9])
    l4 = ListNode.from_list([9, 9])
    
    result2 = add_two_numbers(l3, l4)
    print(f"\nInput: {l3.to_list()} + {l4.to_list()}")
    print(f"Output: {result2.to_list() if result2 else []}")
    print(f"Expected: [8, 9, 0, 1]")

