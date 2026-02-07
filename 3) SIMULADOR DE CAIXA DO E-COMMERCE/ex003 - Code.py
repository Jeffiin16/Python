# Importa todas as funções do pacote utilidades
from utilidades import *

# Nome do arquivo onde os produtos serão armazenados
arquivo = 'produtos.txt'

# Verifica se o arquivo existe
# Caso não exista, ele é criado
if not arquivoExiste(arquivo):
  criarArquivo(arquivo)

# Loop principal do programa (menu infinito)
while True:

  # Exibe o menu de opções para o usuário
  mostrarMenu([
      'VERIFICAR PRODUTOS CADASTRADOS',
      'CADASTRAR NOVO PRODUTO',
      'ALTERAR PRODUTO JÁ CADASTRADO',
      'EXCLUIR PRODUTO',
      'SAIR DO PROGRAMA'
  ])

  # Lê a opção digitada pelo usuário (inteiro validado)
  escolha = leiaInt('Sua escolha: ')

  # Validação para garantir que a opção esteja entre 1 e 5
  while escolha > 5 or escolha < 1:
      print('\033[1;32mERRO! Escolha uma opção válida.\033[m') 
      escolha = leiaInt('Sua escolha: ')

  # OPÇÃO 1 – Listar produtos cadastrados
  if escolha == 1:
    cabeçalho('PRODUTOS CADASTRADOS')  # Exibe título formatado
    lerArquivo(arquivo)                # Lê e mostra o conteúdo do arquivo

  # OPÇÃO 2 – Cadastrar novo produto
  elif escolha == 2:
    cabeçalho('NOVO CADASTRO')

    # Lê nome do produto e padroniza formatação
    prod = input('Novo produto: ').strip().title()

    # Lê preço validado como float
    price = leiaFloat('Preço: ')

    # Substitui "ç" por "c" para evitar problemas de encoding
    # e grava o produto no arquivo
    cadastrarNovo(arquivo, prod.replace('ç', 'c'), price)

  # OPÇÃO 3 – Alterar produto existente
  elif escolha == 3:
    cabeçalho('ALTERAR PRODUTO')
    print('Qual produto deseja alterar?')

    # Mostra lista atual de produtos
    lerArquivo(arquivo)

    # Usuário escolhe qual item alterar
    opc = leiaInt('Sua opção: ')

    # Função responsável por editar o produto escolhido
    alterarProduto(arquivo, opc)

  # OPÇÃO 4 – Excluir produto
  elif escolha == 4:
    cabeçalho('EXCLUSÃO DE PRODUTO')
    print('Qual produto deseja excluir?')

    # Mostra lista atual antes da exclusão
    lerArquivo(arquivo)

    # Usuário escolhe qual item remover
    opc = leiaInt('Sua opção: ')

    # Remove o produto selecionado do arquivo
    excluirProduto(arquivo, opc)

  # OPÇÃO 5 – Encerrar programa
  else:
    encerrarPrograma()  # Exibe mensagem/finalização personalizada
    break               # Sai do loop principal