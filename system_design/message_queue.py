"""
Message Queue - System Design Pattern
Producer-Consumer pattern implementation
"""

from collections import deque
from threading import Lock, Condition
from typing import Optional, Any
import time


class MessageQueue:
    """
    Thread-safe message queue implementation
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        max_size: Maximum queue size (None for unlimited)
        """
        self.queue = deque()
        self.max_size = max_size
        self.lock = Lock()
        self.not_empty = Condition(self.lock)
        self.not_full = Condition(self.lock)
    
    def put(self, message: Any, timeout: Optional[float] = None) -> bool:
        """
        Add message to queue
        Returns True if successful, False if timeout
        """
        with self.lock:
            if self.max_size is not None:
                # Wait until space is available
                end_time = time.time() + timeout if timeout else None
                while len(self.queue) >= self.max_size:
                    if timeout and time.time() >= end_time:
                        return False
                    self.not_full.wait(timeout=0.1)
            
            self.queue.append(message)
            self.not_empty.notify()
            return True
    
    def get(self, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Get message from queue
        Returns None if timeout
        """
        with self.lock:
            end_time = time.time() + timeout if timeout else None
            while not self.queue:
                if timeout and time.time() >= end_time:
                    return None
                self.not_empty.wait(timeout=0.1)
            
            message = self.queue.popleft()
            self.not_full.notify()
            return message
    
    def size(self) -> int:
        """Get current queue size"""
        with self.lock:
            return len(self.queue)
    
    def empty(self) -> bool:
        """Check if queue is empty"""
        with self.lock:
            return len(self.queue) == 0


class PriorityQueue:
    """
    Priority message queue (higher priority first)
    """
    
    def __init__(self):
        self.queue = []
        self.lock = Lock()
    
    def put(self, message: Any, priority: int = 0):
        """
        Add message with priority
        Higher priority = processed first
        """
        with self.lock:
            self.queue.append((priority, message))
            self.queue.sort(reverse=True, key=lambda x: x[0])
    
    def get(self) -> Optional[Any]:
        """Get highest priority message"""
        with self.lock:
            if not self.queue:
                return None
            return self.queue.pop(0)[1]
    
    def size(self) -> int:
        with self.lock:
            return len(self.queue)


# Example usage
if __name__ == "__main__":
    # Basic message queue
    print("=== Basic Message Queue ===")
    mq = MessageQueue(max_size=5)
    
    # Producer
    for i in range(10):
        success = mq.put(f"Message {i}")
        print(f"Put message {i}: {'Success' if success else 'Failed (queue full)'}")
    
    # Consumer
    print("\nConsuming messages:")
    for _ in range(10):
        message = mq.get(timeout=1.0)
        if message:
            print(f"  Got: {message}")
    
    # Priority queue
    print("\n=== Priority Queue ===")
    pq = PriorityQueue()
    pq.put("Low priority", priority=1)
    pq.put("High priority", priority=10)
    pq.put("Medium priority", priority=5)
    
    print("Messages in priority order:")
    while pq.size() > 0:
        print(f"  {pq.get()}")

