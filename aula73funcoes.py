def saudacao(msg, nome):
  return f'{msg}, {nome}!'

def executa(funcao, *args):
  return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Andrei'))

print(executa(saudacao, 'Boa noite', 'Nayara'))