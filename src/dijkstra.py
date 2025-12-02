import heapq
import math
from typing import Dict, List, Tuple, Optional


def dijkstra(graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:

    # Inicializa distâncias
    dist: Dict[int, float] = {v: math.inf for v in graph.vertices()}
    parent: Dict[int, Optional[int]] = {v: None for v in graph.vertices()}
    dist[source] = 0.0
    
    # Min-heap com (distância, vértice)
    pq: List[Tuple[float, int]] = [(0.0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Se distância é maior que registrada, ignora
        if d > dist[u]:
            continue
        
        # Relaxa arestas
        for v, w in graph.adj.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    
    return dist, parent
