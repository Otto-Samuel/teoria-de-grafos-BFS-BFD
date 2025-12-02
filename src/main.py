import math
import random
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# Importar algoritmos dos módulos específicos
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from bfs_dfs_simple import bfs, dfs


# ==============================
# CLASSE GRAPH SIMPLES
# ==============================
class Graph:
    # Grafo simples com lista de adjacência
    def __init__(self, directed: bool = False):
        self.adj: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u: int, v: int, w: float = 1.0):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))
    
    def vertices(self) -> List[int]:
        s = set(self.adj.keys())
        for u in list(self.adj.keys()):
            for v, _ in self.adj[u]:
                s.add(v)
        return sorted(s)
    
    def edges(self) -> List[Tuple[int, int, float]]:
        res = []
        for u in self.adj:
            for v, w in self.adj[u]:
                res.append((u, v, w))
        return res


# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def reconstruct_path(parent: Dict[int, Optional[int]], target: int) -> List[int]:
    if target not in parent:
        return []
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path


def print_distances(dist: Dict[int, float]):
    """Exibe distâncias de forma formatada."""
    for v in sorted(dist.keys()):
        dv = dist[v]
        if dv == math.inf:
            print(f"  {v}: unreachable")
        else:
            print(f"  {v}: {dv:.2f}")


# ==============================
# GERADOR DE GRAFO DEMO
# ==============================

def generate_demo_graph(
    num_vertices: int = 16,
    directed: bool = False,
    weighted: bool = True,
    seed: Optional[int] = 42
) -> Graph:
    
    random.seed(seed)
    g = Graph(directed=directed)
    
    # Cria anel de conectividade básica
    for i in range(num_vertices):
        j = (i + 1) % num_vertices
        w = random.uniform(1, 10) if weighted else 1.0
        g.add_edge(i, j, round(w, 2))
    
    # Adiciona arestas aleatórias extras
    extra = max(1, num_vertices // 2)
    for _ in range(extra * 2):
        u = random.randrange(0, num_vertices)
        v = random.randrange(0, num_vertices)
        if u == v:
            continue
        w = random.uniform(1, 15) if weighted else 1.0
        g.add_edge(u, v, round(w, 2))
    
    return g


# ==============================
# PROGRAMA PRINCIPAL - DEMO
# ==============================

def demo():
    print("Gerando grafo demo com 16 vértices...")
    g = generate_demo_graph(16, directed=False, weighted=True)
    print("Amostra de arestas (u -> [(v, peso), ...]):")
    for u in sorted(g.adj.keys())[:8]:
        print(f"  {u}: {g.adj[u]}")
    
    # ===== BFS =====
    print("\n" + "=" * 80)
    print("1️⃣  BFS (Busca em Amplitude)".center(80))
    print("=" * 80)
    parent_bfs = bfs(g, 0)
    print("Pais (parent) da BFS (primeiros 10 vértices):")
    for k in list(parent_bfs.keys())[:10]:
        print(f"  Vértice {k:2d}: parent = {parent_bfs[k]}")
    
    # ===== DFS =====
    print("\n" + "=" * 80)
    print("2️⃣  DFS (Busca em Profundidade)".center(80))
    print("=" * 80)
    parent_dfs, order = dfs(g, 0)
    print("Ordem de descoberta (primeiros 12 vértices):")
    print("  " + " → ".join([str(v) for v in order[:12]]))
    print(f"  ... (total de {len(order)} vértices visitados)")
    
    # ===== DIJKSTRA =====
    print("\n" + "=" * 80)
    print("3️⃣  DIJKSTRA (Caminho Mais Curto - Pesos Positivos)".center(80))
    print("=" * 80)
    dist_dij, parent_dij = dijkstra(g, 0)
    print("Distâncias mais curtas da origem (vértice 0):")
    print_distances(dist_dij)
    print(f"\nExemplo: Caminho mais curto para vértice 7:")
    path = reconstruct_path(parent_dij, 7)
    print(f"  {' → '.join([str(v) for v in path])} (distância: {dist_dij[7]:.2f})")
    
    # ===== BELLMAN-FORD =====
    print("\n" + "=" * 80)
    print("4️⃣  BELLMAN-FORD (Caminho Mais Curto - Pesos Negativos)".center(80))
    print("=" * 80)
    dist_bf, parent_bf = bellman_ford(g, 0)
    if dist_bf is None:
        print("⚠️  CICLO NEGATIVO DETECTADO!")
        print("    O grafo contém um ciclo com peso total negativo.")
    else:
        print("Distâncias mais curtas da origem (vértice 0):")
        print_distances(dist_bf)
        print(f"\nExemplo: Caminho até vértice 7:")
        path = reconstruct_path(parent_bf, 7)
        print(f"  {' → '.join([str(v) for v in path])} (distância: {dist_bf[7]:.2f})")
    
    # ===== RESUMO =====
    print("\n" + "=" * 80)
    print("RESUMO COMPARATIVO".center(80))
    print("=" * 80)
    print("""
┌─────────────┬───────────────┬──────────────┬──────────────────────┐
│ Algoritmo   │ Complexidade  │ Pesos Neg.   │ Melhor para          │
├─────────────┼───────────────┼──────────────┼──────────────────────┤
│ BFS         │ O(V + E)      │ ❌ Não       │ Caminho curto (não-p)│
│ DFS         │ O(V + E)      │ ❌ Não       │ Ciclos, Topologia    │
│ Dijkstra    │ O((V+E)logV)  │ ❌ Não       │ Caminho curto (+)    │
│ Bellman-Ford│ O(V × E)      │ ✅ Sim       │ Ciclos negativos     │
└─────────────┴───────────────┴──────────────┴──────────────────────┘
    """)


if __name__ == "__main__":
    demo()
