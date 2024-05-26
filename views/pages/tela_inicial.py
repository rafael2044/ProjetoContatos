import customtkinter as ctk
from PIL import Image
from views.pages.tela_cadContato import CadContato
class TelaInicial(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configurarTitulo()
        self.configurarGeometria()
        self.carregarWidgets()
        self.mainloop()
    def configurarGeometria(self):
        WIDTH = 600
        HEIGHT = 800

        pos_x = (self.winfo_screenwidth() - WIDTH) // 2
        pos_y = (self.winfo_screenheight() - HEIGHT) // 2

        self.geometry(f"{WIDTH}x{HEIGHT}+{pos_x}+{pos_y}")

    def configurarTitulo(self):
        self.title("Contatos")

    def criarWidgets(self):
        self.limparWidgets()
        self.iconBusca = ctk.CTkImage(Image.open('assets/icons/lupa.png'), size=(32,32))

        self.frameMenu = ctk.CTkFrame(self)
        self.frameContatos = ctk.CTkScrollableFrame(self)

        self.frameBusca = ctk.CTkFrame(self.frameMenu, corner_radius=50, fg_color='#404040', height=40)
        self.lbIconBuscar = ctk.CTkLabel(self.frameBusca,text='', image=self.iconBusca)
        self.entryBuscar = ctk.CTkEntry(self.frameBusca, height=40,
                                        fg_color='#404040', bg_color='#404040', border_color="#404040")
        self.btAdicionar = ctk.CTkButton(self.frameMenu, text='+', height=40, width=50, fg_color='#6d28d9',
                                         hover_color='#8b5cf6', corner_radius=30, command=self.abrirCadastroContato)

    def carregarWidgets(self):
        self.criarWidgets()
        self.frameMenu.pack(fill=ctk.X)
        self.frameContatos.pack(expand=True, fill=ctk.BOTH)
        self.frameBusca.pack(fill=ctk.BOTH, expand=True, side=ctk.LEFT, padx=10, pady=10)
        self.lbIconBuscar.pack(side=ctk.LEFT, padx=5)
        self.entryBuscar.pack(fill=ctk.X, side=ctk.LEFT, expand=True, padx=10)
        self.btAdicionar.pack(side=ctk.LEFT, padx=5)

    def carregarContatos(self):
        pass

    def abrirCadastroContato(self):
        self.limparWidgets()
        CadContato(self).pack(fill=ctk.BOTH,expand=True)

    def limparWidgets(self):
        for w in self.winfo_children():
            w.destroy()