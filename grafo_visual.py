import networkx as nx
import matplotlib.pyplot as plt
from GRAFO import Grafo
def visualizar_grafo(grafo):
    # Criação do grafo usando NetworkX
    G = nx.DiGraph() if grafo.direcionado else nx.Graph()
    
    # Adiciona os vértices ao grafo de NetworkX
    try:
        for vertice in grafo.vertices:
            G.add_node(vertice.nome, weight=str(vertice.tags))
    except Exception:
        for vertice in grafo.vertices:
            G.add_node(vertice.nome, weight=str(vertice.peso))

    
    # Adiciona as arestas ao grafo de NetworkX
    for vertice in grafo.vertices:
        for aresta in vertice.arestas:
            v1 = aresta.vertice1.nome
            v2 = aresta.vertice2.nome
            if grafo.direcionado or (not grafo.direcionado and vertice == aresta.vertice1):
                G.add_edge(v1, v2, weight=aresta.peso)

    # Extrai os pesos dos vértices e arestas para visualização
    node_weights = nx.get_node_attributes(G, "weight")
    edge_weights = nx.get_edge_attributes(G, "weight")
    
    # Desenho do grafo
    pos = nx.spring_layout(G)  # Layout para posicionar os nós
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10, font_color="black")
    
   
    #if edge_weights:
        #nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_size=8)

    # Exibe os pesos dos vértices (se existirem)
    for node, (x, y) in pos.items():
        weight = node_weights.get(node, None)
        if weight is not None:
            plt.text(x, y + 0.1, f"({weight})", fontsize=8, ha="center", color="green")

    plt.title("Representação Visual do Grafo")
    plt.show()


