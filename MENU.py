import tkinter as tk
from tkinter import messagebox
from GRAFO import Grafo
from tkinter import simpledialog
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import tkinter.simpledialog as simpledialog
from TGRAFO import TGrafo
from caminho_hamiltoniano import  HamiltonianPathFinder
from Caminho_euleriano import EulerianPathFinder
from Coloraçao import GraphColoring
from Salvar_grafo import salvar_grafo_em_txt
from grafo_visual import visualizar_grafo
from TGRAFO import TGrafo
from leitura_arquivo_txt import  carregar_grafo_modelado
from leitura_pasta_videos import lerClips

class GraphApp:
    def __init__(self, root):
        self.grafo = Grafo()
        self.root = root
        self.root.title("Gerenciador de clipes de seguraca por meio de Grafo")
        
        # Criar botões
        self.create_buttons()

    def create_buttons(self):
        
        buttons = [
            ("Ler dados de Pasta de Clips", self.clips),
            ("Navegacao pelo Grafo de Clips", self.navegacao),
            ("Ler dados do arquivo grafo.txt", self.ler_dados),
            ("Gravar dados no arquivo grafo.txt", self.gravar_dados),
            ("Inserir vértice", self.inserir_vertice),
            ("Inserir aresta", self.inserir_aresta),
            ("Remove vértice", self.remove_vertice),
            ("Remove aresta", self.remove_aresta),
            ("Mostrar grafo", self.mostrar_grafo),
            ("Informacoes", self.informacoes),
            ("Encerrar a aplicação", self.encerrar_aplicacao),
        ]

        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command, width=40, padx=10, pady=5)
            button.pack(pady=5)
    def clips(self):
        self.grafo =  lerClips("clips segurança")
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")
    def navegacao(self):
        
        VideoPlayer(self.root, self.grafo,)
        #root.mainloop()
    def informacoes(self):
        messagebox.showinfo("informacoes", "Essa aplicacao foi feita Por Francesco Zangrandi Coppola")

    def ler_dados(self):
        self.grafo = carregar_grafo_modelado("GRAFO.txt")
        
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")

    def gravar_dados(self):
        salvar_grafo_em_txt(self.grafo, "GRAFO.txt", tipo_grafo=1)
        messagebox.showinfo("Ação", "Gravar dados no arquivo grafo.txt")

    def inserir_vertice(self):
        try:
            self.grafo.addVertice(str(self.grafo.verticesNum +1))
        except Exception:
            self.grafo.addTVertice(str(self.grafo.verticesNum +1))
        
        messagebox.showinfo("sucesso", f"vertice inserido: {self.grafo.verticesNum }")


    def inserir_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        vertice1=self.grafo.getVertice(vertice1)
        vertice2=self.grafo.getVertice(vertice2)
        
        try:
            self.grafo.addAresta(vertice1,vertice2)
        except Exception:
            self.grafo.addTAresta(vertice1,vertice2)
        messagebox.showinfo("sucesso", "aresta inserida")

    def remove_vertice(self):
        vertice = simpledialog.askinteger("Qual vertice quer remover", "Digite o nome do vertice:")
        vertice=self.grafo.getVertice(vertice)
        self.grafo.remover_vertice(vertice)
        messagebox.showinfo("sucesso", "vertice "  +str(vertice)+" removido")

    def remove_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        vertice1=self.grafo.getVertice(vertice1)
        vertice2=self.grafo.getVertice(vertice2)
        self.grafo.remove_aresta(vertice1,vertice2)
       
        messagebox.showinfo("sucesso", "aresta removida")

  
        

    def mostrar_grafo(self):
        self.grafo.print()
        messagebox.showinfo("sucesso", "grafo exibido em pronpt de commando")

    
       

    def encerrar_aplicacao(self):
        self.root.quit()

class VideoPlayer:
    def __init__(self, window, grafo):
        self.window = window
        self.window.title("Video Player")
        self.grafo = grafo
        # Inicializa a lista de fontes de vídeo
        self.video_sources=[]
        self.video_sources.append(grafo.clips[3])
        self.current_video_index = 0
        self.vid = cv2.VideoCapture(self.video_sources[self.current_video_index]) if self.video_sources else None
        # Adiciona vídeos com base nas condições
        self.populate_video_sources(0,self.video_sources)

        # Carregar vídeo, se houver fontes
        

        # Criar um rótulo para exibir o vídeo
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH) if self.vid else 640,
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT) if self.vid else 480)
        self.canvas.pack()

        # Criar botões para trocar vídeos
        self.buttons_frame = tk.Frame(window)
        self.buttons_frame.pack()
        self.update_buttons()

        self.update()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        


    def populate_video_sources(self,clip,aux):
       
        clip = self.grafo.clips.index(aux[clip])
        
        #self.remove_all_videos()

        video_sources = [self.grafo.clips[clip]]
        if self.grafo.clips[clip] in self.grafo.arquivos_pessoa:
            for x in range(len(self.grafo.arquivos_pessoa)):
                if(self.grafo.arquivos_pessoa[x] in   video_sources):
                    continue
                video_sources.append(self.grafo.arquivos_pessoa[x])
        if self.grafo.clips[clip] in self.grafo.arquivos_animal:
            for x in range(len(self.grafo.arquivos_animal)):
                video_sources.append(self.grafo.arquivos_animal[x])
        if self.grafo.clips[clip] in self.grafo.arquivos_carro:
            for x in range(len(self.grafo.arquivos_carro)):
                video_sources.append(self.grafo.arquivos_carro[x])
        
        self.video_sources = video_sources

    def create_video_buttons(self):
        for index, video in enumerate(self.video_sources):
            button = tk.Button(self.buttons_frame, text=f"Vídeo {index + 1}", command=lambda i=index: self.switch_video(i))
            button.pack(side=tk.LEFT)

    def update(self):
        if self.vid is not None:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

    def update_buttons(self):
        # Limpar botões existentes
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Criar botões para cada vídeo na lista
        for index, video in enumerate(self.video_sources):
            button = tk.Button(self.buttons_frame, text=f"Vídeo {index + 1}", command=lambda i=index: self.switch_video(i))
            button.pack(side=tk.LEFT)
    def switch_video(self, index):
        if self.vid is not None:
            self.vid.release()  # Libere o vídeo atual
        aux = []
        aux = self.video_sources
        aux2=aux
        # Limpar vídeos atuais e repopular a lista
        self.remove_all_videos()
        self.populate_video_sources(index,aux2)
        
        if self.video_sources:  # Verifica se há vídeos disponíveis
            self.current_video_index = index
            self.vid = cv2.VideoCapture(self.video_sources[self.current_video_index])
            self.update_buttons()
              # Carregue o novo vídeo
        else:
            self.vid = None  # Se não há vídeos, define como None
            self.canvas.delete("all")  # Limpa o canvas se não houver vídeos

    def remove_all_videos(self):
        if self.vid is not None:
            self.vid.release()  # Libere o vídeo atual
        self.video_sources = [] # Limpa a lista de vídeos
        self.current_video_index = 0  # Reseta o índice atual
        self.canvas.delete("all")  # Limpa o canvas

    def on_closing(self):
        # Liberar a fonte de vídeo e destruir a janela
        if self.vid is not None:
            self.vid.release()
        self.window.destroy()
root = tk.Tk()
app = GraphApp(root)
root.mainloop()