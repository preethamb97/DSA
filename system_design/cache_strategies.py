"""
Cache Strategies - System Design Patterns
LRU, LFU, FIFO, and Time-based expiration
"""

from typing import Optional, Dict, Any
from collections import OrderedDict
from datetime import datetime, timedelta
import time


class FIFOCache:
    """
    First In First Out Cache
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: str) -> Optional[Any]:
        """Get value by key"""
        return self.cache.get(key)
    
    def put(self, key: str, value: Any) -> None:
        """Put key-value pair"""
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove oldest (first) item
            self.cache.popitem(last=False)
        
        self.cache[key] = value


class LFUCache:
    """
    Least Frequently Used Cache
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[str, Any] = {}
        self.freq: Dict[str, int] = {}
        self.min_freq = 0
    
    def get(self, key: str) -> Optional[Any]:
        """Get value by key"""
        if key not in self.cache:
            return None
        
        # Update frequency
        self.freq[key] = self.freq.get(key, 0) + 1
        return self.cache[key]
    
    def put(self, key: str, value: Any) -> None:
        """Put key-value pair"""
        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            self.freq[key] = self.freq.get(key, 0) + 1
        else:
            if len(self.cache) >= self.capacity:
                # Remove least frequently used
                lfu_key = min(self.freq.keys(), key=lambda k: self.freq[k])
                del self.cache[lfu_key]
                del self.freq[lfu_key]
            
            self.cache[key] = value
            self.freq[key] = 1


class TimeBasedCache:
    """
    Time-based expiration cache
    """
    
    def __init__(self, default_ttl: int = 3600):
        """
        default_ttl: Default time-to-live in seconds
        """
        self.cache: Dict[str, tuple] = {}
        self.default_ttl = default_ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get value by key (returns None if expired)"""
        if key not in self.cache:
            return None
        
        value, expiry_time = self.cache[key]
        
        if datetime.now() > expiry_time:
            # Expired, remove it
            del self.cache[key]
            return None
        
        return value
    
    def put(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Put key-value pair with optional TTL"""
        ttl = ttl or self.default_ttl
        expiry_time = datetime.now() + timedelta(seconds=ttl)
        self.cache[key] = (value, expiry_time)
    
    def cleanup(self) -> int:
        """Remove expired entries, return count removed"""
        now = datetime.now()
        expired_keys = [
            key for key, (_, expiry) in self.cache.items()
            if now > expiry
        ]
        
        for key in expired_keys:
            del self.cache[key]
        
        return len(expired_keys)


# Example usage
if __name__ == "__main__":
    # FIFO Cache
    print("=== FIFO Cache ===")
    fifo = FIFOCache(capacity=3)
    for i in range(5):
        fifo.put(f"key{i}", f"value{i}")
        print(f"After putting key{i}: {list(fifo.cache.keys())}")
    
    # LFU Cache
    print("\n=== LFU Cache ===")
    lfu = LFUCache(capacity=3)
    lfu.put("a", 1)
    lfu.put("b", 2)
    lfu.put("c", 3)
    lfu.get("a")  # Access 'a' twice
    lfu.get("a")
    lfu.get("b")  # Access 'b' once
    lfu.put("d", 4)  # Should evict 'c' (least frequently used)
    print(f"Cache after eviction: {list(lfu.cache.keys())}")
    
    # Time-based Cache
    print("\n=== Time-based Cache ===")
    tbc = TimeBasedCache(default_ttl=2)  # 2 second TTL
    tbc.put("temp", "data")
    print(f"Get immediately: {tbc.get('temp')}")
    time.sleep(3)
    print(f"Get after 3 seconds: {tbc.get('temp')}")  # Should be None

