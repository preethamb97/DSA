"""
Unit tests for LRU Cache
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dsa.design_patterns.lru_cache import LRUCache


class TestLRUCache:
    """Test cases for LRU Cache"""
    
    def test_basic_operations(self):
        """Test basic get and put operations"""
        lru = LRUCache(2)
        
        lru.put(1, 1)
        lru.put(2, 2)
        
        assert lru.get(1) == 1
        assert lru.get(2) == 2
    
    def test_eviction(self):
        """Test that least recently used item is evicted"""
        lru = LRUCache(2)
        
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(3, 3)  # Should evict key 1
        
        assert lru.get(1) == -1  # Evicted
        assert lru.get(2) == 2
        assert lru.get(3) == 3
    
    def test_update_existing_key(self):
        """Test updating existing key doesn't evict"""
        lru = LRUCache(2)
        
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(1, 10)  # Update key 1
        lru.put(3, 3)  # Should evict key 2, not key 1
        
        assert lru.get(1) == 10
        assert lru.get(2) == -1  # Evicted
        assert lru.get(3) == 3
    
    def test_get_updates_lru(self):
        """Test that get operation updates LRU order"""
        lru = LRUCache(2)
        
        lru.put(1, 1)
        lru.put(2, 2)
        lru.get(1)  # Access key 1, making it recently used
        lru.put(3, 3)  # Should evict key 2, not key 1
        
        assert lru.get(1) == 1
        assert lru.get(2) == -1  # Evicted
        assert lru.get(3) == 3
    
    def test_capacity_one(self):
        """Test cache with capacity 1"""
        lru = LRUCache(1)
        
        lru.put(1, 1)
        assert lru.get(1) == 1
        
        lru.put(2, 2)  # Should evict key 1
        assert lru.get(1) == -1
        assert lru.get(2) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

