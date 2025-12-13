"""
Load Balancer - System Design Pattern
Round Robin, Least Connections, Weighted Round Robin
"""

from typing import List, Dict
from collections import defaultdict
import random


class Server:
    """Represents a backend server"""
    
    def __init__(self, id: str, weight: int = 1):
        self.id = id
        self.weight = weight
        self.active_connections = 0
        self.total_requests = 0
    
    def handle_request(self):
        """Handle a request"""
        self.active_connections += 1
        self.total_requests += 1
    
    def complete_request(self):
        """Complete a request"""
        self.active_connections -= 1


class RoundRobinBalancer:
    """Round Robin Load Balancer"""
    
    def __init__(self, servers: List[Server]):
        self.servers = servers
        self.current_index = 0
    
    def get_server(self) -> Server:
        """Get next server in round-robin fashion"""
        if not self.servers:
            raise ValueError("No servers available")
        
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server


class LeastConnectionsBalancer:
    """Least Connections Load Balancer"""
    
    def __init__(self, servers: List[Server]):
        self.servers = servers
    
    def get_server(self) -> Server:
        """Get server with least active connections"""
        if not self.servers:
            raise ValueError("No servers available")
        
        return min(self.servers, key=lambda s: s.active_connections)


class WeightedRoundRobinBalancer:
    """Weighted Round Robin Load Balancer"""
    
    def __init__(self, servers: List[Server]):
        self.servers = servers
        self.current_weight = 0
        self.current_index = -1
    
    def get_server(self) -> Server:
        """Get next server based on weights"""
        if not self.servers:
            raise ValueError("No servers available")
        
        while True:
            self.current_index = (self.current_index + 1) % len(self.servers)
            
            if self.current_index == 0:
                self.current_weight -= min(s.weight for s in self.servers)
                if self.current_weight <= 0:
                    self.current_weight = sum(s.weight for s in self.servers)
            
            if self.servers[self.current_index].weight >= self.current_weight:
                return self.servers[self.current_index]


class IPHashBalancer:
    """IP Hash Load Balancer (Sticky Sessions)"""
    
    def __init__(self, servers: List[Server]):
        self.servers = servers
    
    def get_server(self, client_ip: str) -> Server:
        """Get server based on client IP hash"""
        if not self.servers:
            raise ValueError("No servers available")
        
        hash_value = hash(client_ip)
        index = hash_value % len(self.servers)
        return self.servers[index]


# Example usage
if __name__ == "__main__":
    # Create servers
    servers = [
        Server("server1", weight=3),
        Server("server2", weight=2),
        Server("server3", weight=1)
    ]
    
    # Round Robin
    print("=== Round Robin ===")
    rr_balancer = RoundRobinBalancer(servers)
    for i in range(6):
        server = rr_balancer.get_server()
        print(f"Request {i+1} -> {server.id}")
    
    # Least Connections
    print("\n=== Least Connections ===")
    lc_balancer = LeastConnectionsBalancer(servers)
    servers[0].active_connections = 3
    servers[1].active_connections = 1
    servers[2].active_connections = 2
    
    for i in range(5):
        server = lc_balancer.get_server()
        server.handle_request()
        print(f"Request {i+1} -> {server.id} (connections: {server.active_connections})")
    
    # Weighted Round Robin
    print("\n=== Weighted Round Robin ===")
    wrr_balancer = WeightedRoundRobinBalancer(servers)
    for i in range(12):
        server = wrr_balancer.get_server()
        print(f"Request {i+1} -> {server.id} (weight: {server.weight})")

