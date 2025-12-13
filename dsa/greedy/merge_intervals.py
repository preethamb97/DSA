"""
Merge Intervals - LeetCode #56
Frequency: 85% (Extremely common)

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Sort and merge overlapping intervals
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # If current overlaps with last, merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Insert Interval - LeetCode #57
    Insert new_interval into intervals and merge if necessary
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Non-overlapping Intervals - LeetCode #435
    Return minimum number of intervals to remove
    """
    if not intervals:
        return 0
    
    # Sort by end time (greedy: keep intervals that end earliest)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        # If current interval overlaps with previous
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count


# Test cases
if __name__ == "__main__":
    # Test Merge Intervals
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = merge(intervals1)
    print(f"Merge {intervals1}:")
    print(f"  Result: {result1}")  # Expected: [[1, 6], [8, 10], [15, 18]]
    
    # Test Insert Interval
    intervals2 = [[1, 3], [6, 9]]
    new = [2, 5]
    result2 = insert_interval(intervals2, new)
    print(f"\nInsert {new} into {intervals2}:")
    print(f"  Result: {result2}")  # Expected: [[1, 5], [6, 9]]
    
    # Test Erase Overlap
    intervals3 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result3 = erase_overlap_intervals(intervals3)
    print(f"\nErase overlaps from {intervals3}:")
    print(f"  Remove {result3} intervals")  # Expected: 1

