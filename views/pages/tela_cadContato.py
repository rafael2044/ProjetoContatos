import customtkinter as ctk

class CadContato(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.criarWidgets()
        self.carregarWidgets()


    def criarWidgets(self):
        self.frameBotoes = ctk.CTkFrame(self, fg_color='transparent')
        self.frameImagem = ctk.CTkFrame(self, corner_radius=100)
        self.frameDados = ctk.CTkFrame(self, fg_color='transparent')


        self.btFechar = ctk.CTkButton(self.frameBotoes, text='X',command=self.master.carregarWidgets, width=30, height=30,
                                      fg_color='#6d28d9', hover_color='#8b5cf6', corner_radius=30)
    def carregarWidgets(self):
        self.frameBotoes.pack(fill=ctk.X)
        self.frameImagem.pack()
        self.frameDados.pack(fill=ctk.BOTH, expand=True)
        self.btFechar.pack(side=ctk.LEFT, padx=10, pady=10)