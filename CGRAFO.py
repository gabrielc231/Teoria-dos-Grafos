from TGRAFO import TGrafo
from TGRAFO import TaggedVertice

class CVertice(TaggedVertice):
        def __init__(self, nome,clip = None,tag=None,color=None):
            self.color = color
            super().__init__(nome,clip,tag,color=None)
        def changeColor(self, color):
             self.color = color
        
        





class CGrafo(TGrafo):
    def __init__(self,direcionado = False, nome = "CGRAFO"):
        super().__init__(direcionado,nome)
        
    
    def addVertice(self, nome,clip = None ,tag = None,color = None):
        vertice = CVertice(nome,clip,tag,color)
        self.vertices.append(vertice)
        self.verticesNum += 1  
        
                 
        return vertice
    
    def changeColor(self,V,color):
        V.color = color
         
    



