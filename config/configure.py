from assets.database.database import db
from models.contato import Contato

def configure_all():
    configure_db(db)
def configure_db(db):
    with db:
        db.create_tables([Contato])
        #dados_teste()
        #retornar_dados()
def dados_teste():
    contatos = [
        {
            "nome": "Luiz",
            "sobrenome": "Souza",
            "empresa": "Empresa ABC",
            "telefone": "11111111",
            "marcador_telefone": "celular",
            "celular": "999999999",
            "email": "luiz.souza@example.com",
            "obs": "Novo cliente"
        },
        {
            "nome": "Ana",
            "sobrenome": "Lima",
            "empresa": "Empresa XYZ",
            "telefone": "22222222",
            "marcador_telefone": "comercial",
            "celular": "888888888",
            "email": "ana.lima@example.com",
            "obs": "Parceira de longa data"
        },
        {
            "nome": "Pedro",
            "sobrenome": "Ferreira",
            "empresa": "Empresa 123",
            "telefone": "33333333",
            "marcador_telefone": "principal",
            "celular": "777777777",
            "email": "pedro.ferreira@example.com",
            "obs": "Fornecedor confiável"
        },
        {
            "nome": "Mariana",
            "sobrenome": "Alves",
            "empresa": "Empresa XYZ",
            "telefone": "44444444",
            "marcador_telefone": "casa",
            "celular": "666666666",
            "email": "mariana.alves@example.com",
            "obs": "Contato importante"
        },
        {
            "nome": "Paulo",
            "sobrenome": "Oliveira",
            "empresa": "Empresa ABC",
            "telefone": "55555555",
            "marcador_telefone": "celular",
            "celular": "555555555",
            "email": "paulo.oliveira@example.com",
            "obs": "Cliente antigo"
        },
        {
            "nome": "Cristina",
            "sobrenome": "Pereira",
            "empresa": "Empresa 123",
            "telefone": "66666666",
            "marcador_telefone": "comercial",
            "celular": "444444444",
            "email": "cristina.pereira@example.com",
            "obs": "Parceira de negócios"
        },
        {
            "nome": "Roberto",
            "sobrenome": "Santos",
            "empresa": "Empresa XYZ",
            "telefone": "77777777",
            "marcador_telefone": "casa",
            "celular": "333333333",
            "email": "roberto.santos@example.com",
            "obs": "Novo contato"
        },
        {
            "nome": "Isabela",
            "sobrenome": "Costa",
            "empresa": "Empresa 123",
            "telefone": "88888888",
            "marcador_telefone": "principal",
            "celular": "222222222",
            "email": "isabela.costa@example.com",
            "obs": "Cliente VIP"
        },
        {
            "nome": "Renato",
            "sobrenome": "Rodrigues",
            "empresa": "Empresa ABC",
            "telefone": "99999999",
            "marcador_telefone": "celular",
            "celular": "111111111",
            "email": "renato.rodrigues@example.com",
            "obs": "Parceiro estratégico"
        },
        {
            "nome": "Leticia",
            "sobrenome": "Gomes",
            "empresa": "Empresa XYZ",
            "telefone": "10101010",
            "marcador_telefone": "comercial",
            "celular": "999999999",
            "email": "leticia.gomes@example.com",
            "obs": "Cliente potencial"
        }
    ]

    for contato in contatos:
        Contato.create(**contato)

    print("Dados inseridos")

def retornar_dados():
    rows = Contato.select()
    for row in rows:
        print(f"")

