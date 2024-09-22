from GrafoMatriz import Grafo

# Teste 1
graph1 = Grafo(4)
graph1.insereAV(0, 1, 20)
graph1.insereAV(0, 2, 30)
graph1.insereAV(0, 3, 50)
graph1.insereAV(1, 0, 20)
graph1.insereAV(1, 2, 40)
graph1.insereAV(1, 3, 15)
graph1.insereAV(2, 0, 30)
graph1.insereAV(2, 1, 40)
graph1.insereAV(2, 3, 15)
graph1.insereAV(3, 0, 50)
graph1.insereAV(3, 1, 15)
graph1.insereAV(3, 2, 15)

# Executando Dijkstra a partir do vértice 1
print("Teste 1:")
distancias1 = graph1.dijkstra(1)
print("Distâncias a partir do vértice 1:", distancias1)

# Teste 2
graph2 = Grafo(5)
graph2.insereAV(0, 1, 1)
graph2.insereAV(0, 4, 1)
graph2.insereAV(1, 2, 1)
graph2.insereAV(1, 3, 2)
graph2.insereAV(2, 3, 4)
graph2.insereAV(2, 4, 2)
graph2.insereAV(3, 0, 3)
graph2.insereAV(4, 0, 2)
graph2.insereAV(4, 3, 1)

# Executando Dijkstra a partir do vértice 0
print("Teste 2:")
distancias2 = graph2.dijkstra(0)
print("Distâncias a partir do vértice 0:", distancias2)