import peewee as pw
from assets.database.database import db
MARCADORES = (
    ('celular', 'Celular'),
    ('comercial', 'Comercial'),
    ('casa', 'Casa'),
    ('principal', 'Principal')
)

class Contato(pw.Model):
    nome = pw.CharField(max_length=30)
    sobrenome = pw.CharField(max_length=50)
    empresa = pw.CharField(max_length=80)
    telefone = pw.CharField(max_length=10)
    marcador_telefone = pw.CharField(choices=MARCADORES)
    celular = pw.CharField(max_length=11)
    email = pw.CharField(max_length=200)
    obs = pw.TextField()

    class Meta:
        database = db