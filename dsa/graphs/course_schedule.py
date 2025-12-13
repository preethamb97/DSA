"""
Course Schedule - LeetCode #207, #210
Frequency: 75% (Very common - Topological Sort)

There are a total of numCourses courses you have to take. Some courses have prerequisites.
Determine if you can finish all courses and return the order.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List, Dict, Set
from collections import defaultdict, deque


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Course Schedule I - Check if can finish all courses
    Uses topological sort (Kahn's algorithm)
    """
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Find all courses with no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        
        # Remove this course and update dependencies
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Course Schedule II - Return the order to take courses
    """
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Find all courses with no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        # Remove this course and update dependencies
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # If we couldn't complete all courses, return empty list
    return order if len(order) == num_courses else []


def can_finish_dfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    DFS approach with cycle detection
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses
    
    def has_cycle(course: int) -> bool:
        if state[course] == 1:  # Cycle detected
            return True
        if state[course] == 2:  # Already processed
            return False
        
        state[course] = 1  # Mark as visiting
        
        for next_course in graph[course]:
            if has_cycle(next_course):
                return True
        
        state[course] = 2  # Mark as visited
        return False
    
    # Check all courses
    for course in range(num_courses):
        if state[course] == 0 and has_cycle(course):
            return False
    
    return True


# Test cases
if __name__ == "__main__":
    # Test Course Schedule I
    num_courses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = can_finish(num_courses1, prerequisites1)
    print(f"Can finish {num_courses1} courses: {result1}")  # True
    
    num_courses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]  # Cycle
    result2 = can_finish(num_courses2, prerequisites2)
    print(f"Can finish {num_courses2} courses (with cycle): {result2}")  # False
    
    # Test Course Schedule II
    num_courses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result3 = find_order(num_courses3, prerequisites3)
    print(f"Order for {num_courses3} courses: {result3}")  # [0, 1, 2, 3] or [0, 2, 1, 3]

