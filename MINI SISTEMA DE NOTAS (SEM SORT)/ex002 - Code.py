from utilidades import *

notas = [] # começa com lista vazia

for i in range(0, 4):
  n = leiaFloat(f'Digite a {i+1}ª nota: ')
  if i == 0: # 4. Se for o primeiro valor a ser informado/digitado, só adiciona
    notas.append(n)
  else:
    inseriu = False # Criamos uma variável para marcar se já inserimos
    for x in notas: # Percorremos a lista comparando
      if n < x:
        notas.insert(notas.index(x), n)
        inseriu = True # marca que inseriu
        break # para o loop, não precisa comparar mais
    if not inseriu: # Se NÃO inseriu no loop, significa que é maior que todos
      notas.append(n)

print(f'Notas ordenadas: {notas}')
print(f'Maior nota: {max(notas)}')
print(f'Média: {sum(notas) / len(notas):.2f}')
