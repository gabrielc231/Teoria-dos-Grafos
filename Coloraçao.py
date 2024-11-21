from GRAFO import Grafo
class GraphColoring:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.color_map = {}

    def color_graph(self):
        # Ordena os vértices em ordem arbitrária (ou pelo grau, se preferir)
        vertices = self.grafo.vertices
        self.color_map = {}

        # Atribui cores aos vértices
        for vertice in vertices:
            # Descobre as cores usadas pelos vizinhos
            used_colors = set()
            for aresta in vertice.arestas:
                neighbor = aresta.vertice2 if aresta.vertice1 == vertice else aresta.vertice1
                if neighbor in self.color_map:
                    used_colors.add(self.color_map[neighbor])

            # Atribui a menor cor disponível
            color = 0
            while color in used_colors:
                color += 1
            self.color_map[vertice] = color

        return self.color_map

    def print_coloring(self):
        for vertice, color in self.color_map.items():
            print(f"Vértice {vertice.nome}: Cor {color}")


# Exemplo de uso:
grafo = Grafo()

# Adicionando vértices
v1 = grafo.addVertice("A")
v2 = grafo.addVertice("B")
v3 = grafo.addVertice("C")
v4 = grafo.addVertice("D")

# Adicionando arestas
grafo.addAresta(v1, v2)
grafo.addAresta(v2, v3)
grafo.addAresta(v3, v4)
grafo.addAresta(v4, v1)
grafo.addAresta(v1, v3)

# Imprime o grafo
grafo.print()

# Realiza a coloração do grafo
coloring = GraphColoring(grafo)
color_map = coloring.color_graph()

# Exibe a coloração
coloring.print_coloring()
