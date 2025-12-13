"""
LRU Cache - LeetCode #146
Frequency: 85% (Extremely common - System Design)

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

from typing import Optional


class ListNode:
    """Doubly linked list node"""
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache using HashMap + Doubly Linked List
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head and tail for easier operations
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: ListNode):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: ListNode):
        """Remove an existing node"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node: ListNode):
        """Move node to head (mark as recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self) -> Optional[ListNode]:
        """Remove last node (LRU)"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        """Get value by key"""
        node = self.cache.get(key)
        
        if not node:
            return -1
        
        # Move to head (mark as recently used)
        self._move_to_head(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        """Insert or update value"""
        node = self.cache.get(key)
        
        if not node:
            # New key
            new_node = ListNode(key, value)
            
            if len(self.cache) >= self.capacity:
                # Remove LRU
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            self._add_node(new_node)
        else:
            # Update existing
            node.val = value
            self._move_to_head(node)


# Test cases
if __name__ == "__main__":
    lru = LRUCache(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"Get 1: {lru.get(1)}")  # Returns 1
    
    lru.put(3, 3)  # Evicts key 2
    print(f"Get 2: {lru.get(2)}")  # Returns -1 (not found)
    
    lru.put(4, 4)  # Evicts key 1
    print(f"Get 1: {lru.get(1)}")  # Returns -1 (not found)
    print(f"Get 3: {lru.get(3)}")  # Returns 3
    print(f"Get 4: {lru.get(4)}")  # Returns 4

