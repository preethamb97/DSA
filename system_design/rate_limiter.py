"""
Rate Limiter - System Design Pattern
Token Bucket and Sliding Window implementations
"""

from collections import deque
from typing import Dict
import time
from threading import Lock


class TokenBucket:
    """
    Token Bucket Rate Limiter
    Allows bursts up to bucket capacity
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        """
        capacity: Maximum tokens in bucket
        refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = Lock()
    
    def allow_request(self, tokens: int = 1) -> bool:
        """Check if request is allowed"""
        with self.lock:
            self._refill()
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
    
    def _refill(self):
        """Refill tokens based on time elapsed"""
        now = time.time()
        elapsed = now - self.last_refill
        tokens_to_add = elapsed * self.refill_rate
        
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now


class SlidingWindowLog:
    """
    Sliding Window Log Rate Limiter
    Tracks requests in time windows
    """
    
    def __init__(self, max_requests: int, window_seconds: int):
        """
        max_requests: Maximum requests allowed
        window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()
        self.lock = Lock()
    
    def allow_request(self) -> bool:
        """Check if request is allowed"""
        with self.lock:
            now = time.time()
            
            # Remove requests outside window
            while self.requests and self.requests[0] < now - self.window_seconds:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True
            return False


class RateLimiter:
    """
    Multi-user rate limiter using token bucket
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets: Dict[str, TokenBucket] = {}
        self.lock = Lock()
    
    def allow_request(self, user_id: str, tokens: int = 1) -> bool:
        """Check if user's request is allowed"""
        with self.lock:
            if user_id not in self.buckets:
                self.buckets[user_id] = TokenBucket(self.capacity, self.refill_rate)
            
            return self.buckets[user_id].allow_request(tokens)


# Example usage
if __name__ == "__main__":
    # Token Bucket example
    print("=== Token Bucket ===")
    bucket = TokenBucket(capacity=10, refill_rate=2.0)  # 2 tokens/second
    
    for i in range(15):
        allowed = bucket.allow_request()
        print(f"Request {i+1}: {'Allowed' if allowed else 'Rate Limited'}")
        time.sleep(0.1)
    
    # Sliding Window example
    print("\n=== Sliding Window ===")
    window = SlidingWindowLog(max_requests=5, window_seconds=1)
    
    for i in range(10):
        allowed = window.allow_request()
        print(f"Request {i+1}: {'Allowed' if allowed else 'Rate Limited'}")
        time.sleep(0.1)
    
    # Multi-user rate limiter
    print("\n=== Multi-User Rate Limiter ===")
    limiter = RateLimiter(capacity=5, refill_rate=1.0)
    
    for user_id in ['user1', 'user2']:
        for i in range(7):
            allowed = limiter.allow_request(user_id)
            print(f"{user_id} Request {i+1}: {'Allowed' if allowed else 'Rate Limited'}")

