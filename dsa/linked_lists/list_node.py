"""
ListNode class for linked list problems
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list"""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        result = []
        current = self
        visited = set()
        
        while current and id(current) not in visited:
            visited.add(id(current))
            result.append(str(current.val))
            current = current.next
            if current and id(current) in visited:
                result.append("... (cycle)")
                break
        
        return " -> ".join(result) if result else "None"
    
    @classmethod
    def from_list(cls, values: list) -> Optional['ListNode']:
        """Create linked list from Python list"""
        if not values:
            return None
        
        head = cls(values[0])
        current = head
        
        for val in values[1:]:
            current.next = cls(val)
            current = current.next
        
        return head
    
    def to_list(self) -> list:
        """Convert linked list to Python list"""
        result = []
        current = self
        visited = set()
        
        while current and id(current) not in visited:
            visited.add(id(current))
            result.append(current.val)
            current = current.next
            if current and id(current) in visited:
                break
        
        return result

