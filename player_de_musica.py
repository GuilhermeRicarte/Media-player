import tkinter as tk
from tkinter import filedialog
import pygame

# Inicializa o Pygame
pygame.mixer.init()

# Variáveis globais
musica_atual = None
reproduzindo = False

# Funções para controlar a música
def abrir_musica():
    global musica_atual
    arquivo = filedialog.askopenfilename(
        initialdir="/",
        title="Selecione um arquivo de música",
        filetypes=(("Arquivos de música", "*.mp3 *.wav"), ("Todos os arquivos", "*.*"))
    )
    if arquivo:
        musica_atual = arquivo
        pygame.mixer.music.load(musica_atual)
        titulo_musica.config(text=f"Tocando: {musica_atual}")

def tocar_pausar():
    global reproduzindo
    if reproduzindo:
        pygame.mixer.music.pause()
        botao_tocar.config(text="Tocar")
    else:
        pygame.mixer.music.play()
        botao_tocar.config(text="Pausar")
    reproduzindo = not reproduzindo

def parar():
    global reproduzindo
    pygame.mixer.music.stop()
    reproduzindo = False
    botao_tocar.config(text="Tocar")
    titulo_musica.config(text="Nenhuma música tocando")

# Cria a janela principal
janela = tk.Tk()
janela.title("Reprodutor de Música")

# Cria os botões
botao_abrir = tk.Button(janela, text="Abrir Música", command=abrir_musica)
botao_tocar = tk.Button(janela, text="Tocar", command=tocar_pausar)
botao_parar = tk.Button(janela, text="Parar", command=parar)

# Cria a label para exibir o título da música
titulo_musica = tk.Label(janela, text="Nenhuma música tocando")

# Posiciona os elementos na janela
botao_abrir.pack()
botao_tocar.pack()
botao_parar.pack()
titulo_musica.pack()

# Inicia a janela
janela.mainloop()

