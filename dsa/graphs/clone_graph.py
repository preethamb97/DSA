"""
Clone Graph - LeetCode #133
Frequency: 80% (Very common - Meta favorite)

Given a reference of a node in a connected undirected graph,
return a deep copy (clone) of the graph.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional, Dict, List


class Node:
    """Graph node definition"""
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """
    DFS approach with hash map
    """
    if not node:
        return None
    
    visited: Dict[Node, Node] = {}
    
    def dfs(original: Node) -> Node:
        if original in visited:
            return visited[original]
        
        # Create clone
        clone = Node(original.val)
        visited[original] = clone
        
        # Clone neighbors
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    BFS approach
    """
    if not node:
        return None
    
    from collections import deque
    
    visited: Dict[Node, Node] = {}
    queue = deque([node])
    visited[node] = Node(node.val)
    
    while queue:
        original = queue.popleft()
        clone = visited[original]
        
        for neighbor in original.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            
            clone.neighbors.append(visited[neighbor])
    
    return visited[node]


# Test cases
if __name__ == "__main__":
    # Create graph: [[2,4],[1,3],[2,4],[1,3]]
    #    1 -- 2
    #    |    |
    #    4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned = clone_graph_dfs(node1)
    print(f"Original node1 value: {node1.val}")
    print(f"Cloned node1 value: {cloned.val if cloned else None}")
    print(f"Cloned neighbors count: {len(cloned.neighbors) if cloned else 0}")

