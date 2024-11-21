from GRAFO import Vertice
from GRAFO import Aresta
from GRAFO import Grafo
def elementos_iguais(a, b):
    # Convertendo 'a' e 'b' para conjuntos
    if isinstance(a, list):
        conjunto_a = set(a)  # Mantém os elementos da lista
    else:
        conjunto_a = set(a)  # Se for string, cada caractere vira um elemento

    if isinstance(b, list):
        conjunto_b = set(b)  # Mantém os elementos da lista
    else:
        conjunto_b = set(b)  # Se for string, cada caractere vira um elemento
    
    # Retornando a interseção dos dois conjuntos
    return list(conjunto_a.intersection(conjunto_b))

class TagsNaoExistentes(Exception):
    pass


class VerticesNaoExistentes(Exception):
    pass




class TaggedVertice(Vertice):
    def __init__(self, nome, clip,tag=None):
       
        super().__init__(nome)
        self.clip = clip 
        self.tags = tag  
    
    


class TGrafo(Grafo) :

    def __init__(self,direcionado = False, nome = "TGRAFO"):
        super().__init__(direcionado,nome)
    
    def addTVertice(self, nome,clip = "test",tag = None):
        vertice = TaggedVertice(nome,clip,tag)
        self.vertices.append(vertice)
        self.verticesNum += 1  
        return vertice
    
    def addVertice(self, nome,clip = "test",tag = None):
        vertice = TaggedVertice(nome,clip,tag)
        self.vertices.append(vertice)
        self.verticesNum += 1  
        return vertice
    
    def addAresta(self, v1:Vertice ,v2 :Vertice , peso=1):
        aresta = TaggedAresta()
        
        if(v1 in self.vertices and v2 in self.vertices):
            aresta.conectar(v1, v2,peso)  
            aresta.peso = peso 
            aresta.direcionado = self.direcionado  
            v1.addAresta(aresta)  
            if not self.direcionado:
                v2.addAresta(aresta)
            self.arestasNum += 1  
            return aresta
        else:
            raise VerticesNaoExistentes("Error message")
   
    
    def addTAresta(self, v1:Vertice ,v2 :Vertice , peso=1):
        aresta = TaggedAresta()
        
        if(v1 in self.vertices and v2 in self.vertices):
            aresta.conectar(v1, v2,peso)  
            aresta.peso = peso 
            aresta.direcionado = self.direcionado  
            v1.addAresta(aresta)  
            if not self.direcionado:
                v2.addAresta(aresta)
            self.arestasNum += 1  
            return aresta
        else:
            raise VerticesNaoExistentes("Error message")
    
    def conectar_all_tags(self):
        for v1 in  self.vertices :
            for v2 in  self.vertices :
                aresta = TaggedAresta()
                if(v1 == v2):
                    continue

                
                if(v1 in self.vertices and v2 in self.vertices):
                    if aresta.conectar(v1, v2):
                        aresta.peso = 1
                        aresta.direcionado = self.direcionado  
                        v1.addAresta(aresta)  
                        
                        self.arestasNum += 1  
    


            
        


class TaggedAresta(Aresta):
    def __init__(self,tags=None):
       
        super().__init__()
        self.tags = tags 

    
    def addTag(self,tag):
        try:
            self.tags.append(tag)
        except Exception:
            self.tags=tag 
    
    def print(self):
        if self.direcionado:
            print(f"[ {self.vertice1}({elementos_iguais(self.vertice1.tags,self.vertice2.tags)}) ---> ({elementos_iguais(self.vertice1.tags,self.vertice2.tags)}){self.vertice2} , Peso: {self.peso} ]", end=" , ")
        else:
            print(f"[ {self.vertice1}({elementos_iguais(self.vertice1.tags,self.vertice2.tags)}) ---- ({elementos_iguais(self.vertice1.tags,self.vertice2.tags)}){self.vertice2} , Peso: {self.peso} ]", end=" , ")



    def conectar(self,v1 : TaggedVertice ,v2 : TaggedVertice,peso = 1):
        tag1 = v1.tags
        tag2 = v2.tags
        self.peso = peso
        bothTags =elementos_iguais(tag1,tag2)
        
       
       
        if len(bothTags) !=0:
            self.tags = bothTags
            self.vertice1 = v1 
            self.vertice2 = v2 
            return True
        else:
            return False
           
    
  

        

    
