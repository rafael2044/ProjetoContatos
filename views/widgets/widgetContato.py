from customtkinter import CTkFrame, CTkLabel, CTkFont, LEFT, BOTH, CTkImage
from PIL import Image, ImageTk
from base64 import b64decode
import random
from controllers.functions import adicionarBordaCircular

class WidgetContato(CTkFrame):
    def __init__(self, master, contato):
        super().__init__(master=master)
        self.inicial = contato.nome[0]
        self.contato = contato
        self.configurarFrame()
        self.criarWidgets()
        self.carregarWidgets()

    def configurarFrame(self):
        self.configure(height=100)
        self.configure(width=100)
        self.configure(corner_radius=100)
    def criarWidgets(self):
        cores = [
            '#b91c1c', '#450a0a', '#c2410c', '#431407', '#fbbf24', '#a16207', '#4d7c0f', '#1a2e05',
            '#22c55e', '#15803d', '#14532d', '#059669', '#064e3b', '#14b8a6', '#0f766e', '#134e4a',
            '#0891b2', '#155e75', '#083344', '#0284c7', '#1e40af', '#1e1b4b', '#4338ca', '#5b21b6',
            '#9333ea', '#a21caf', '#701a75', '#4a044e', '#be185d', '#e11d48', '#881337', '#292524',
            '#27272a', '#111827'
        ]
        fontContato = CTkFont('Roboto-Regular', size=18)
        fontInicial = CTkFont('Roboto-Bold', size=30, weight='bold')

        self.frameImg = CTkFrame(self, corner_radius=150, bg_color='transparent', fg_color='transparent', width=80, height=80)
        self.imgContato = CTkLabel(self.frameImg, text='', font=fontInicial,bg_color='transparent', fg_color='transparent')
        if not self.contato.foto:
            self.imgContato.configure(text=self.inicial)
            self.frameImg.configure(fg_color=cores[random.randint(0, len(cores) - 1)])
        else:
            self.imgContato.configure(image=CTkImage(adicionarBordaCircular(self.contato.foto), size=(50,50)))
            self.frameImg.configure(fg_color='transparent')

        self.lbNomeCompleto = CTkLabel(self, text=f"{self.contato.nome} {self.contato.sobrenome}", font=fontContato)

    def carregarWidgets(self):
        self.frameImg.pack(side=LEFT, padx=15,pady=15)
        self.frameImg.pack_propagate(0)
        self.imgContato.pack(padx=15, pady=15, fill='both', expand=True)
        self.lbNomeCompleto.pack(side=LEFT)

        func_enter = lambda event: self.configure(fg_color='#6b7280')
        func_leave = lambda event: self.configure(fg_color=['gray81', 'gray20'])

        self.frameImg.bind('<Enter>', func_enter)
        self.frameImg.bind('<Leave>', func_leave)
        self.imgContato.bind('<Enter>', func_enter)
        self.imgContato.bind('<Leave>', func_leave)
        self.lbNomeCompleto.bind('<Enter>', func_enter)
        self.lbNomeCompleto.bind('<Leave>', func_leave)
        self.bind('<Enter>', func_enter)
        self.bind('<Leave>', func_leave)
