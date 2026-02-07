def leiaFloat(msg=''):
  # Lê a entrada do usuário removendo espaços extras
  num = input(msg).strip()

  # Loop até o usuário digitar um valor válido
  while True:

    # Evita número começando com ponto (ex: ".5")
    if num[0] == '.':
      print(f'\033[1;32mERRO! Digite um valor válido para a nota.\033[m')
      num = input(msg)

    # Caso use ponto como separador decimal
    if num.replace('.', '').isnumeric():
      num = float(num)
      break

    # Caso use vírgula como separador decimal
    elif num.replace(',', '').isnumeric():
      num = float(num.replace(',', '.'))
      break

    # Entrada inválida
    else:
      print(f'\033[1;32mERRO! Digite um valor válido para a nota.\033[m')
      num = input(msg)

  return num  # Retorna número float validado


def leiaInt(msg):
  # Lê entrada do usuário
  num = input(msg)

  # Loop até ser um número inteiro válido
  while True:
    if num.isnumeric():
      num = int(num)
      break
    else:
      print('\033[1;32mERRO! Digite um número inteiro válido.\033[m')
      num = input(msg)

  return num  # Retorna inteiro validado


def mostrarMenu(list):
  # Mostra o cabeçalho do sistema
  cabeçalho('SISTEMA E-COMMERCE')

  cont = 1  # Contador para numeração das opções

  # Percorre a lista de opções exibindo numerado
  for i in list:
    print(f'[ {cont} ] {i}')
    cont += 1


def linha():
  # Imprime linha decorativa colorida
  print('\033[1;35m-\033[m' * 60)


def cabeçalho(text):
  # Exibe título centralizado entre duas linhas
  linha()
  print(text.center(60))
  linha()


def encerrarPrograma():
  # Import local para usar pausa
  from time import sleep

  linha()
  print('\033[1;35mEncerrando o programa', end='')

  # Animação de pontos
  sleep(0.8); print('.', end='')
  sleep(0.8); print('.', end='')
  sleep(0.8); print('.')

  sleep(2)
  print('PROGRAMA FINALIZADO')
  linha()


def arquivoExiste(nome):
  # Tenta abrir o arquivo apenas para leitura
  try:
    arq = open(nome, 'rt')
    arq.close()
  except FileNotFoundError:
    return False  # Não existe
  else:
    return True   # Existe


def criarArquivo(nome):
  # Cria arquivo de texto caso não exista
  try: 
    arq = open(nome, 'wt+')
  except:
    print('Houve um problema na criação do arquivo.')
  else:
    print(f'Arquivo {nome} criado com sucesso!')
  finally:
    arq.close()


def lerArquivo(nome):
  # Lê todo o conteúdo do arquivo
  try:
    arq = open(nome, 'rt')
    linha = arq.readlines()
  except:
    print('Erro ao ler o arquivo.')
  else:
    # Percorre cada linha exibindo formatado
    for pos, i in enumerate(linha, start=1):
      i = i.replace('\n', '')   # Remove quebra de linha
      i = i.split(';')          # Separa nome e preço
      print(f'[{pos}] - {i[0]:<40} R${float(i[1]):>6.2f}')
  finally:
    arq.close()


def cadastrarNovo(nome, prod='<desconhecido>', price=0):
  # Abre arquivo em modo de adicionar
  try:
    arq = open(nome, 'at')
  except:
    print('Houve um erro na abertura do arquivo.')
  else:
    try:
      # Salva produto no formato "nome;preço"
      arq.write(f'{prod};{price}\n')
    except:
      print('Houve um erro na hora de escrever os dados.')
    else:
      print(f'\033[1;35m{prod}\033[m cadastrado com sucesso!')
  finally:
    arq.close()


def alterarProduto(nome, escolha):
  # Lê todo o arquivo
  try:
    arq = open(nome, 'rt')
    linha = arq.readlines()
    arq.close()
  except:
    print('Houve um problema na hora de alterar o arquivo.')
  else:
    nova_lista = []

    # Novos dados do produto
    nome_prod = input('Digite o nome do novo produto: ').strip().title()
    preco_prod = leiaFloat('Preço: ')

    # Recria lista substituindo apenas o escolhido
    for pos, conteudo in enumerate(linha, start=1):
      if escolha == pos:
        nova_lista.append(f'{nome_prod};{preco_prod}\n')
      else:
        nova_lista.append(conteudo)

    # Reescreve o arquivo com a nova lista
    try:
      arq = open(nome, 'wt')
      arq.writelines(nova_lista)
    except:
      print('Houve um erro ao salvar alteração.')
    finally:
      arq.close()

    print(f'\033[1;35mProduto alterado com sucesso!\033[m')


def excluirProduto(nome, escolha):
  # Lê o arquivo completo
  try:
    arq = open(nome, 'rt')
    linha = arq.readlines()
    arq.close()
  except:
    print('Houve um erro na hora de excluir o produto do arquivo.')
  else:
    nova_lista = []

    # Mantém apenas os produtos diferentes do escolhido
    for pos, produto in enumerate(linha, start=1):
      if pos != escolha:
        nova_lista.append(produto)

    # Reescreve o arquivo sem o item excluído
    try:
      arq = open(nome, 'wt')
      arq.writelines(nova_lista)
    except:
      print('Houve um erro ao excluir o produto.')
    finally:
      arq.close()

    print(f'\033[1;35mProduto excluido com sucesso!\033[m')