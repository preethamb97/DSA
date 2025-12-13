"""
Top K Frequent Elements - LeetCode #347
Frequency: 80% (Very common)

Given an integer array nums and an integer k, return the k most frequent elements.

Time Complexity: O(n log k) with heap, O(n) with bucket sort
Space Complexity: O(n)
"""

from typing import List
from collections import Counter, defaultdict
import heapq


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Heap approach: O(n log k) time
    """
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap of size k
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        
        # Keep only k elements
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract results
    return [num for _, num in heap]


def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    """
    Bucket sort approach: O(n) time
    """
    count = Counter(nums)
    n = len(nums)
    
    # Bucket: index = frequency, value = list of numbers
    buckets = defaultdict(list)
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Extract top k from buckets
    result = []
    for freq in range(n, 0, -1):
        if freq in buckets:
            result.extend(buckets[freq])
            if len(result) >= k:
                break
    
    return result[:k]


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Kth Largest Element - LeetCode #215
    Find the kth largest element in an unsorted array
    """
    # Use min heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge K Sorted Lists - LeetCode #23 (simplified to return sorted list)
    Merge k sorted linked lists (here simplified to lists)
    """
    heap = []
    
    # Add first element of each list to heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(
                heap,
                (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            )
    
    return result


# Test cases
if __name__ == "__main__":
    # Test Top K Frequent
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = top_k_frequent_heap(nums1, k1)
    print(f"Top {k1} frequent in {nums1}: {result1}")  # Expected: [1, 2]
    
    # Test Kth Largest
    nums2 = [3, 2, 1, 5, 6, 4]
    k2 = 2
    result2 = find_kth_largest(nums2, k2)
    print(f"{k2}th largest in {nums2}: {result2}")  # Expected: 5
    
    # Test Merge K Sorted
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    result3 = merge_k_sorted_lists(lists)
    print(f"Merged {lists}: {result3}")  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

