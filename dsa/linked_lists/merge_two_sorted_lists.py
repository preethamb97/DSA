"""
Merge Two Sorted Lists - LeetCode #21
Frequency: 90% (Extremely common)

Merge two sorted linked lists and return it as a sorted list.

Time Complexity: O(m + n)
Space Complexity: O(1) iterative, O(m + n) recursive
"""

from typing import Optional
from .list_node import ListNode


def merge_two_lists(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Iterative approach: O(1) space
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes
    current.next = list1 if list1 else list2
    
    return dummy.next


def merge_two_lists_recursive(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Recursive approach: O(m + n) space
    """
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge K Sorted Lists - LeetCode #23
    Merge k sorted linked lists
    """
    if not lists:
        return None
    
    # Divide and conquer approach
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))
        
        lists = merged_lists
    
    return lists[0]


# Test cases
if __name__ == "__main__":
    # Test Merge Two Lists
    list1 = ListNode.from_list([1, 2, 4])
    list2 = ListNode.from_list([1, 3, 4])
    
    result = merge_two_lists(list1, list2)
    print(f"Merge {list1.to_list()} and {list2.to_list()}:")
    print(f"Result: {result.to_list() if result else []}")
    print(f"Expected: [1, 1, 2, 3, 4, 4]")
    
    # Test Merge K Lists
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6])
    ]
    
    result2 = merge_k_lists(lists)
    print(f"\nMerge {len(lists)} lists:")
    print(f"Result: {result2.to_list() if result2 else []}")
    print(f"Expected: [1, 1, 2, 3, 4, 4, 5, 6]")

