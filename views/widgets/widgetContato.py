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
        self.configure(corner_radius=30)
    def criarWidgets(self):
        cores = [
            "#dcdcdc", "#d3d3d3", "#90ee90", "#20b2aa", "#b0c4de", "#d8bfd8", "#f5deb3", "#ffffff"
        ]

        self.frameImg = CTkFrame(self, corner_radius=100, bg_color='transparent', fg_color=cores[random.randint(0, len(cores)-1)])
        self.lbInicial = CTkLabel(self.frameImg, text=self.inicial, font=CTkFont('arial', size=30, weight='bold'),
                                  width=50, height=50, bg_color='transparent', fg_color='transparent')

        self.lbNomeCompleto = CTkLabel(self, text=f"{self.contato.nome} {self.contato.sobrenome}", font=CTkFont('arial', size=15))

    def carregarWidgets(self):
        self.frameImg.pack(side=LEFT, padx=10,pady=5)
        self.lbInicial.pack(padx=5, pady=5)
        self.lbNomeCompleto.pack(side=LEFT)

        self.frameImg.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.frameImg.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.lbInicial.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.lbInicial.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.lbNomeCompleto.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.lbNomeCompleto.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
        self.bind('<Enter>', lambda event: self.configure(fg_color='#6b7280'))
        self.bind('<Leave>', lambda event: self.configure(fg_color=["gray85", "gray16"]))
