from GRAFO import Grafo
class EulerianPathFinder:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.path = []

    def is_eulerian(self):
        # Verifica o número de vértices com grau ímpar
        odd_vertices = [v for v in self.grafo.vertices if len(v.arestas) % 2 != 0]
        return len(odd_vertices) == 2 or len(odd_vertices) == 0, odd_vertices

    def remove_aresta(self, v1, v2):
        # Remove uma aresta entre dois vértices
        for aresta in v1.arestas:
            if (aresta.vertice1 == v1 and aresta.vertice2 == v2) or (aresta.vertice1 == v2 and aresta.vertice2 == v1):
                v1.arestas.remove(aresta)
                if not self.grafo.direcionado:
                    v2.arestas.remove(aresta)
                return

    def find_eulerian_path_util(self, vertice):
        # Visita cada aresta exatamente uma vez
        for aresta in list(vertice.arestas):  # Copia a lista para evitar modificação durante a iteração
            proximo_vertice = aresta.vertice2 if aresta.vertice1 == vertice else aresta.vertice1
            self.remove_aresta(vertice, proximo_vertice)
            self.find_eulerian_path_util(proximo_vertice)
        self.path.append(vertice)

    def find_eulerian_path(self):
        is_eulerian, odd_vertices = self.is_eulerian()
        if not is_eulerian:
            print("O grafo não tem um caminho Euleriano.")
            return None

        # Começa de um vértice com grau ímpar, se existir, ou qualquer vértice
        start_vertex = odd_vertices[0] if len(odd_vertices) == 2 else self.grafo.vertices[0]
        self.path = []
        self.find_eulerian_path_util(start_vertex)
        print("Caminho Euleriano encontrado:")
        print(" -> ".join([v.nome for v in self.path[::-1]]))  # Caminho reverso para ordem correta
        return self.path

