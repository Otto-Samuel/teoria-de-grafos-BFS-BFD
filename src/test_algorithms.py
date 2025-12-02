

from graph import Graph
from bfs_dfs import BFS, DFS
from dijkstra import Dijkstra
from bellman_ford import BellmanFord


def criar_grafo_cidades():
    # Cria o grafo de rede de cidades com 16 vértices.
    g = Graph(16, directed=False)
    
    cidades = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador",
        "Brasília", "Goiânia", "Curitiba", "Porto Alegre",
        "Fortaleza", "Recife", "Manaus", "Belém",
        "Vitória", "Cuiabá", "Campinas", "Londrina"
    ]
    
    for i, city in enumerate(cidades):
        g.set_vertex_name(i, city)
    
    edges = [
        (0, 1, 430), (0, 14, 100), (0, 2, 580), (0, 6, 400),
        (1, 2, 580), (1, 12, 520),
        (2, 3, 1100), (2, 4, 700), (2, 12, 520),
        (3, 8, 1200), (3, 9, 800),
        (4, 5, 200), (4, 13, 900), (4, 2, 700),
        (5, 13, 800), (5, 4, 200),
        (6, 0, 400), (6, 7, 700), (6, 15, 500),
        (7, 6, 700),
        (8, 3, 1200), (8, 9, 600),
        (9, 3, 800), (9, 8, 600), (9, 10, 2600),
        (10, 11, 1700), (10, 9, 2600),
        (11, 10, 1700),
        (12, 2, 520), (12, 1, 520),
        (13, 4, 900), (13, 5, 800),
        (14, 0, 100), (14, 15, 250),
        (15, 6, 500), (15, 14, 250),
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    return g


def teste_bfs():
    # Testa o algoritmo BFS. 
    print("\n" + "="*100)
    print("TESTE 1: BFS (Busca em Amplitude)".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    bfs = BFS(g)
    
    print(f"\nGrafo: Rede de {g.vertices} cidades")
    print(f"Tipo: Não-direcionado")
    print(f"Vértice inicial: {g.vertex_names[0]} (índice 0)")
    
    # Executa BFS
    ordem = bfs.search(0)
    print(f"\nOrdem de visita (nível por nível): {' → '.join([g.vertex_names[v] for v in ordem])}")
    
    # Mostra distâncias
    print("\nDistâncias do vértice inicial:")
    for v in sorted(bfs.distance.keys()):
        print(f"  {g.vertex_names[v]:20} → distância: {bfs.distance[v]}")
    
    # Testa caminho mais curto
    print("\nExemplos de caminhos mais curtos:")
    for target in [3, 7, 10]:
        encontrado, caminho = bfs.find_shortest_path(0, target)
        if encontrado:
            caminho_str = " → ".join([g.vertex_names[v] for v in caminho])
            print(f"  São Paulo → {g.vertex_names[target]}: {caminho_str}")


def teste_dfs():
    # Testa o algoritmo DFS.
    print("\n" + "="*100)
    print("TESTE 2: DFS (Busca em Profundidade)".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    dfs = DFS(g)
    
    print(f"\nGrafo: Rede de {g.vertices} cidades")
    print(f"Tipo: Não-direcionado")
    print(f"Vértice inicial: {g.vertex_names[0]} (índice 0)")
    
    # Executa DFS
    ordem = dfs.search(0)
    print(f"\nOrdem de visita (profundidade): {' → '.join([g.vertex_names[v] for v in ordem])}")
    
    # Mostra tempos
    print("\nTempo de descoberta e conclusão:")
    for v in sorted(dfs.discovery_time.keys()):
        print(f"  {g.vertex_names[v]:20} → descoberta: {dfs.discovery_time[v]:2d}, "
              f"conclusão: {dfs.finish_time[v]:2d}")
    
    # Detecta ciclos
    tem_ciclo = dfs.detect_cycle()
    print(f"\nGrafo contém ciclos: {'Sim' if tem_ciclo else 'Não'}")


def teste_dijkstra():
    print("\n" + "="*100)
    print("TESTE 3: DIJKSTRA (Caminho Mais Curto)".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    dijkstra = Dijkstra(g)
    
    print(f"\nGrafo: Rede de {g.vertices} cidades")
    print(f"Tipo: Não-direcionado com pesos (distâncias em km)")
    print(f"Vértice de origem: {g.vertex_names[0]} (São Paulo)")
    
    # Encontra todos os caminhos mais curtos
    distances = dijkstra.find_shortest_paths(0)
    
    print("\nDistâncias mais curtas de São Paulo para cada cidade:")
    for v in sorted(distances.keys()):
        dist = distances[v]
        dist_str = f"{dist:.0f} km" if dist != float('inf') else "∞"
        print(f"  {g.vertex_names[v]:20} → {dist_str:>10}")
    
    # Exemplos de caminhos
    print("\nExemplos de rotas mais curtas:")
    destinos = [3, 8, 10]
    for target in destinos:
        dist, caminho = dijkstra.find_shortest_path(0, target)
        if dist != float('inf'):
            caminho_str = " → ".join([g.vertex_names[v] for v in caminho])
            print(f"  São Paulo → {g.vertex_names[target]:20} ({dist:.0f} km): {caminho_str}")


def teste_bellman_ford():
    print("\n" + "="*100)
    print("TESTE 4: BELLMAN-FORD (Caminho Mais Curto)".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    bf = BellmanFord(g)
    
    print(f"\nGrafo: Rede de {g.vertices} cidades")
    print(f"Tipo: Não-direcionado com pesos (distâncias em km)")
    print(f"Vértice de origem: {g.vertex_names[0]} (São Paulo)")
    
    # Encontra todos os caminhos mais curtos
    distances = bf.find_shortest_paths(0)
    
    if distances is None:
        print("\n⚠️  CICLO NEGATIVO DETECTADO!")
        return
    
    print("\nDistâncias mais curtas de São Paulo para cada cidade:")
    for v in sorted(distances.keys()):
        dist = distances[v]
        dist_str = f"{dist:.0f} km" if dist != float('inf') else "∞"
        print(f"  {g.vertex_names[v]:20} → {dist_str:>10}")
    
    # Exemplos de caminhos
    print("\nExemplos de rotas mais curtas:")
    destinos = [3, 8, 10]
    for target in destinos:
        dist, caminho = bf.find_shortest_path(0, target)
        if dist != float('inf'):
            caminho_str = " → ".join([g.vertex_names[v] for v in caminho])
            print(f"  São Paulo → {g.vertex_names[target]:20} ({dist:.0f} km): {caminho_str}")
    
    print(f"\nIterações de relaxamento: {len(bf.execution_steps)}")


def teste_comparacao_bfs_dfs():
    """Compara BFS e DFS."""
    print("\n" + "="*100)
    print("TESTE 5: COMPARAÇÃO BFS vs DFS".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    
    bfs = BFS(g)
    dfs = DFS(g)
    
    start = 0
    bfs_ordem = bfs.search(start)
    dfs_ordem = dfs.search(start)
    
    print(f"\nVértice inicial: {g.vertex_names[start]}")
    
    print("\nBFS (Breadth-First):")
    print("  " + " → ".join([g.vertex_names[v] for v in bfs_ordem]))
    
    print("\nDFS (Depth-First):")
    print("  " + " → ".join([g.vertex_names[v] for v in dfs_ordem]))
    
    print("\nCaracterísticas:")
    print(f"  BFS usa: Fila (FIFO)")
    print(f"  DFS usa: Pilha (LIFO)")
    print(f"  Ambos visitam: {len(bfs_ordem)} vértices")
    
    # Mostra níveis do BFS
    bfs_levels = bfs.get_level_order(start)
    print("\nNíveis no BFS (distância do vértice inicial):")
    for level, vertices in bfs_levels.items():
        vertices_names = [g.vertex_names[v] for v in vertices]
        print(f"  Nível {level}: {', '.join(vertices_names)}")


def salvar_grafo():
    """Salva o grafo em JSON."""
    print("\n" + "="*100)
    print("SALVANDO GRAFO EM JSON".center(100))
    print("="*100)
    
    g = criar_grafo_cidades()
    filepath = "../demo_graphs/graph16.json"
    
    try:
        g.save_to_json(filepath)
        print(f"\n✓ Grafo salvo com sucesso em: {filepath}")
    except Exception as e:
        print(f"\n❌ Erro ao salvar: {e}")


def main():
    """Executa todos os testes."""
    print("\n" + "█"*100)
    print("DEMONSTRAÇÃO COMPLETA DE ALGORITMOS DE GRAFOS".center(100))
    print("█"*100)
    
    print("\nEste script demonstra a execução de 4 algoritmos fundamentais")
    print("em um grafo com 16 vértices (rede de cidades brasileiras).")
    
    # Executa cada teste
    teste_bfs()
    teste_dfs()
    teste_dijkstra()
    teste_bellman_ford()
    teste_comparacao_bfs_dfs()
    
    # Salva o grafo
    salvar_grafo()
    
    print("\n" + "█"*100)
    print("TESTES CONCLUÍDOS COM SUCESSO!".center(100))
    print("█"*100 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
