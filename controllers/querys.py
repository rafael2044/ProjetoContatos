from models.contato import Contato
from tkinter import messagebox

def select_all_contatos():
    return Contato.select()

def pesquisar_contatos_por_inicial(letra):
    return Contato.select().where(Contato.nome.startswith(letra))

def insertNovoContato(**kargs):
    try:
        if kargs.get('nome') == '':
            raise ValueError
        Contato.create(**kargs)
        messagebox.showinfo('Sucesso', 'Novo contato inserido com sucesso!')
    except ValueError as ve:
        messagebox.showerror('Erro', 'O campo nome está vazio!')
    except Exception as e:
        print('Ocorreu um erro ao adicionar o novo contato!')
        print(e)
        messagebox.showerror('Erro', 'Ocorreu um erro ao inserir o novo contato!')

