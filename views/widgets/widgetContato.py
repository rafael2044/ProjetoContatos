from customtkinter import CTkFrame, CTkLabel, CTkFont, LEFT, BOTH
import random

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
        fontContato = CTkFont('Roboto-Regular', size=15)
        fontInicial = CTkFont('Roboto-Bold', size=30, weight='bold')

        self.frameImg = CTkFrame(self, corner_radius=100, bg_color='transparent', fg_color=cores[random.randint(0, len(cores)-1)])
        self.lbInicial = CTkLabel(self.frameImg, text=self.inicial, font=fontInicial,
                                  width=50, height=50, bg_color='transparent', fg_color='transparent')

        self.lbNomeCompleto = CTkLabel(self, text=f"{self.contato.nome} {self.contato.sobrenome}", font=fontContato)

    def carregarWidgets(self):
        self.frameImg.pack(side=LEFT, padx=20,pady=20)
        self.lbInicial.pack(padx=10, pady=10)
        self.lbNomeCompleto.pack(side=LEFT)

        self.frameImg.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.frameImg.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.lbInicial.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.lbInicial.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.lbNomeCompleto.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.lbNomeCompleto.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
