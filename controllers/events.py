from controllers.querys import insertNovoContato

def salvarContato(nome, sobrenome, empresa, telefone, marcador_telefone, celular, email, obs, foto):
    novoContato = {'nome':nome, 'sobrenome':sobrenome, 'empresa':empresa, 'telefone':telefone, 'marcador_telefone': marcador_telefone,
                   'celular':celular, 'email':email, 'obs': obs, 'foto':foto}
    insertNovoContato(**novoContato)


