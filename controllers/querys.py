from models.contato import Contato

def select_all_contatos():
    return Contato.select()

def pesquisar_contatos_por_inicial(letra):
    return Contato.select().where(Contato.nome.startswith(letra))