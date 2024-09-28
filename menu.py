import tkinter as tk
from tkinter import messagebox
import grafoMatriz
from tkinter import simpledialog
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import tkinter.simpledialog as simpledialog
class GraphApp:
    def __init__(self, root):
        self.grafo = grafoMatriz.TGrafoND()
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
            ("Mostrar conteúdo do arquivo", self.mostrar_conteudo),
            ("Mostrar grafo", self.mostrar_grafo),
            ("Apresentar a conexidade do grafo e o reduzido", self.apresentar_conexidade),
            ("Informacoes", self.informacoes),
            ("Encerrar a aplicação", self.encerrar_aplicacao),
        ]

        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command, width=40, padx=10, pady=5)
            button.pack(pady=5)
    def clips(self):
        self.grafo = self.grafo.lerClips(r"clips segurança")
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")
    def navegacao(self):
        
        VideoPlayer(self.root, self.grafo,)
        #root.mainloop()
    def informacoes(self):
        messagebox.showinfo("informacoes", "Essa aplicacao foi feita Por Francesco Zangrandi Coppola \n André Franco Raineri\n e Gabriel Gonzaga Chung")

    def ler_dados(self):
        self.grafo = self.grafo.ler("GRAFO.txt")
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")

    def gravar_dados(self):
        self.grafo.gravar_txt()
        messagebox.showinfo("Ação", "Gravar dados no arquivo grafo.txt")

    def inserir_vertice(self):
        
        self.grafo.adicionarV()
        
        
        messagebox.showinfo("sucesso", f"vertice inserido: {self.grafo.n -1}")


    def inserir_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        self.grafo.insereA(vertice1,vertice2)
        
        messagebox.showinfo("sucesso", "aresta inserida")

    def remove_vertice(self):
        vertice = simpledialog.askinteger("Qual vertice quer remover", "Digite o numero do vertice:")
        self.grafo.removeV(vertice)
        messagebox.showinfo("sucesso", "vertice "  +str(vertice)+" removido")

    def remove_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        self.grafo.removeA(vertice1,vertice2)
        self.grafo.removeA(vertice2,vertice1)
        messagebox.showinfo("sucesso", "aresta removida")

    def mostrar_conteudo(self):
        self.grafo.mostra_txt()
        messagebox.showinfo("sucesso", "Grafo exibido em pronpt de commando")
        

    def mostrar_grafo(self):
        self.grafo.show()
        messagebox.showinfo("sucesso", "grafo exibido em pronpt de commando")

    def apresentar_conexidade(self):
        aux = self.grafo.eh_conectado2()
        if(aux):
            messagebox.showinfo("C3", "O grafo e fortemente conexo")
        else:
            messagebox.showinfo("C0", "O grafo e desconexo")
       

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


    

