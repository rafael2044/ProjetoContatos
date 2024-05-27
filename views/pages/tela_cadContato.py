import customtkinter as ctk
from models.contato import MARCADORES
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from controllers.functions import adicionarBordaCircular, converterImagemParaB64
from PIL import Image, ImageTk
from base64 import b64decode
from controllers.events import salvarContato

class CadContato(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.criarWidgets()
        self.carregarWidgets()


    def criarWidgets(self):
        marcadores = [x[1] for x in MARCADORES]
        fontEntry = ctk.CTkFont('Roboto-Regular', size=20)
        fontButton = ctk.CTkFont('Roboto-Regular', size=18)
        confEntry = {'height': 50}
        self.frameBotoes = ctk.CTkFrame(self, fg_color='transparent')
        self.frameImagem = ctk.CTkFrame(self, corner_radius=100)
        self.frameDados = ctk.CTkScrollableFrame(self, fg_color='transparent')
        self.fotoB64 = ''
        self.fotoContato = ctk.CTkLabel(self.frameImagem, text='', bg_color='transparent', fg_color='transparent')

        self.entryNome = ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Primeiro Nome', **confEntry)
        self.entrySobrenome = ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Sobrenome', **confEntry)
        self.entryEmpresa = ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Empresa', **confEntry)
        self.entryTelefone = ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Telefone', **confEntry)
        self.entryMarcTelefone = ctk.CTkComboBox(self.frameDados, font=fontEntry, height=50, values=marcadores,
                                                 state='readonly')
        self.entryMarcTelefone.set(marcadores[0])
        self.entryCelular= ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Celular', **confEntry)
        self.entryEmail = ctk.CTkEntry(self.frameDados, font=fontEntry, placeholder_text='Email', **confEntry)
        self.entryObs = ctk.CTkTextbox(self.frameDados, font=fontEntry)

        self.btFechar = ctk.CTkButton(self.frameBotoes, text='X',command=self.master.carregarWidgets, width=30, height=30,
                                      fg_color='#6d28d9', hover_color='#8b5cf6', corner_radius=30)

        func_salvar = lambda : salvarContato(self.entryNome.get(), self.entrySobrenome.get(),
                                             self.entryEmpresa.get(), self.entryTelefone.get(),
                                             self.entryMarcTelefone.get(), self.entryCelular.get(),
                                             self.entryEmail.get(), self.entryObs.get('0.0', 'end'),
                                             self.fotoB64)

        self.btSalvar = ctk.CTkButton(self.frameDados, text="Salvar",fg_color='#6d28d9', hover_color='#8b5cf6', corner_radius=30,
                                      font=fontButton,
                                      command=func_salvar)
    def carregarWidgets(self):
        self.frameBotoes.pack(fill=ctk.X)
        self.frameImagem.pack()
        ctk.CTkButton(self,text='Adicionar Imagem', fg_color='transparent', bg_color='transparent', border_width=0, hover_color='#8b5cf6',
                      font=ctk.CTkFont('Roboto-Regular', size=14, weight='bold'),
                      command=self.converterImagem).pack(pady=10)
        self.frameDados.pack(fill=ctk.BOTH, expand=True, pady=10)
        self.btFechar.pack(side=ctk.LEFT, padx=10, pady=10)

        entryConfPack = {'padx':30, 'pady':10, 'anchor':ctk.W, 'fill':ctk.X}
        self.entryNome.pack(**entryConfPack)
        self.entrySobrenome.pack(**entryConfPack)
        self.entryEmpresa.pack(**entryConfPack)
        self.entryTelefone.pack(**entryConfPack)
        self.entryMarcTelefone.pack(**entryConfPack)
        self.entryCelular.pack(**entryConfPack)
        self.entryEmail.pack(**entryConfPack)
        ctk.CTkLabel(self.frameDados, text='Observações').pack(anchor=ctk.W)
        self.entryObs.pack(**entryConfPack)
        self.btSalvar.pack(padx=10, anchor=ctk.W, pady=10)

    def converterImagem(self, event=None):
        path_file = askopenfilename(defaultextension='*.jpeg', filetypes=[('Formato PNG', '*.png'),
                                                                         ("Formato JPG", '*jpg'),
                                                                         ("Formato JPEG", '*jpeg')])
        self.fotoB64 = converterImagemParaB64(path_file)
        self.fotoCircular = adicionarBordaCircular(self.fotoB64)

        self.fotoContato.configure(image=ctk.CTkImage(self.fotoCircular, size=(200,200)))
        self.frameImagem.configure(fg_color='transparent')
        self.fotoContato.pack()




