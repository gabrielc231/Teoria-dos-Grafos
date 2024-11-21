
from GRAFO import Grafo
class HamiltonianPathFinder:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.caminho = []

    def is_valid_move(self, vertice, visitados):
        # Verifica se o vértice já foi visitado
        return vertice not in visitados

    def hamiltonian_path_util(self, vertice, visitados):
        # Adiciona o vértice ao caminho
        self.caminho.append(vertice)
        visitados.add(vertice)

        # Se todos os vértices foram visitados, retorna True
        if len(self.caminho) == self.grafo.verticesNum:
            return True

        # Tenta visitar os próximos vértices adjacentes
        for aresta in vertice.arestas:
            proximo_vertice = aresta.vertice2 if aresta.vertice1 == vertice else aresta.vertice1
            if self.is_valid_move(proximo_vertice, visitados):
                if self.hamiltonian_path_util(proximo_vertice, visitados):
                    return True

        # Backtracking: remove o vértice do caminho e da lista de visitados
        self.caminho.pop()
        visitados.remove(vertice)
        return False

    def find_hamiltonian_path(self):
        for vertice in self.grafo.vertices:
            self.caminho = []
            if self.hamiltonian_path_util(vertice, set()):
                print("Caminho Hamiltoniano encontrado:")
                print(" -> ".join([v.nome for v in self.caminho]))
                return self.caminho
        print("Nenhum caminho Hamiltoniano encontrado.")
        return None


