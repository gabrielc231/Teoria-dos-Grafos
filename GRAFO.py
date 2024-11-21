class Aresta:
    def __init__(self, vertice1=None, vertice2=None, peso=1, direcionado=False):
        self.peso = peso
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.direcionado = direcionado

    def conectar(self, v1, v2, peso=1):
        self.vertice1 = v1
        self.vertice2 = v2
        self.peso = peso  # Corrigido para usar o valor correto do peso

    def print(self):
        if self.direcionado:
            print(f"[ {self.vertice1} ---> {self.vertice2} , Peso: {self.peso} ]", end="")
        else:
            print(f"[ {self.vertice1} ---- {self.vertice2} , Peso: {self.peso} ]", end="")


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.arestas = []

    def generateBlankArresta(self):
        aresta = Aresta()
        self.arestas.append(aresta)
        return aresta

    def addAresta(self, aresta: Aresta):
        self.arestas.append(aresta)

    def __str__(self):
        return f"{self.nome}"

    def print(self):
        print(f"{self.nome}:[", end="")
        for aresta in self.arestas:
            aresta.print()
        print("]")
    
    def remover(self):
        for aresta in self.aresta:
            vertice = aresta.vertice2
            for arestas_ligadas in vertice.arestas:
                if(arestas_ligadas.vertice2 ==self):
                    vertice.arestas.remove(arestas_ligadas)




class Grafo:
    def __init__(self, direcionado=False, nome="GRAFO"):
        self.nome = str(nome)
        self.arestasNum = 0
        self.verticesNum = 0
        self.vertices = []
        self.direcionado = direcionado

    def listVertices(self):
        for x in self.vertices :
            print(x)
    
    def getVertice(self,nome):
        
        for x in self.vertices :
            aux=str(x.nome)
            if aux ==str(nome):
                return x
            if x.nome == nome:
                return x
        
    def remover_vertice(self, nome_vertice):
        
       
        for vertice in self.vertices:
            if vertice == nome_vertice:
                vertice_remover = vertice
                
                break
        try:
            self.vertices.remove(vertice_remover)
            self.verticesNum -= 1
            vertice_remover.remover()
        except Exception:
            pass

    def remove_aresta(self,V1,V2):
        for x in  V1.arestas:
            if(x.vertice2 ==V2):
                aux = V1
                V1.arestas.remove(x)
                self.arestasNum -= 1
        
        for x in  V2.arestas:
            if(x.vertice1 ==V1):
                V2.arestas.remove(x)
                

    def addVertice(self, nome):
        vertice = Vertice(nome)
        self.vertices.append(vertice)
        self.verticesNum += 1
        return vertice

    def addAresta(self, v1: Vertice, v2: Vertice, peso=1):
        aresta = Aresta()
        if v1 in self.vertices and v2 in self.vertices:
            aresta.conectar(v1, v2, peso)
            aresta.peso = peso
            aresta.direcionado = self.direcionado
            v1.addAresta(aresta)
            if not self.direcionado:
                v2.addAresta(aresta)
            self.arestasNum += 1
            return aresta
        
       

    def print(self):
        print(f"grafo: {self.nome}")
        print(f"numero de vertices: {self.verticesNum}")
        print(f"numero de Arestas: {self.arestasNum}")
        for v in self.vertices:
            v.print()
            print("\n")



# Teste do código



        