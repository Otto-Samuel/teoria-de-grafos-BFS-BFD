from collections import deque
from typing import Dict, List, Tuple, Optional


def bfs(graph, start: int) -> Dict[int, Optional[int]]:

    parent: Dict[int, Optional[int]] = {}
    visited: set = set()
    q = deque([start])
    visited.add(start)
    parent[start] = None
    
    while q:
        u = q.popleft()
        for v, _ in graph.adj.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    
    return parent


def dfs(graph, start: int) -> Tuple[Dict[int, Optional[int]], List[int]]:

    parent: Dict[int, Optional[int]] = {}
    order: List[int] = []
    visited: set = set()
    
    def visit(u: int, p: Optional[int]):
        visited.add(u)
        parent[u] = p
        order.append(u)
        for v, _ in graph.adj.get(u, []):
            if v not in visited:
                visit(v, u)
    
    visit(start, None)
    return parent, order
