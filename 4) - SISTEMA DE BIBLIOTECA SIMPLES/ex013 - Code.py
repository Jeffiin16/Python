# Importa todas as funções auxiliares do arquivo funcoes.py
# Aqui ficam utilidades como menu, cabeçalho, leitura de arquivo etc.
from funcoes import *

# Nome do arquivo que será usado como "banco de dados" do sistema
arquivo = 'biblioteca.txt'

# Verifica se o arquivo existe.
# Caso não exista, cria automaticamente para evitar erro de leitura depois.
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

# Loop principal do sistema (menu infinito)
# O programa só encerra quando o usuário escolher SAIR.
while True:

    # Pequena pausa para melhorar experiência visual
    sleep(1.5)

    # Exibe o título principal da aplicação
    cabeçalho('BIBLIOTECA', 'amarelo', 'roxo')

    # Exibe o menu com opções disponíveis
    menu(['CADASTRAR LIVRO', 'BUSCAR LIVROS', 'EXCLUIR LIVROS', 'LISTAR LIVROS', 'SAIR'])
    linhaGrossa('roxo')

    # Lê a escolha do usuário
    opc = leiaInt('Sua escolha: ')

    # Validação para garantir que a opção esteja entre 1 e 5
    while opc < 1 or opc > 5:
        print('\033[1;31mERRO!\033[m Digite uma opção válida!')
        opc = leiaInt('Sua opção: ')

    # ===================== OPÇÃO 1 — CADASTRAR =====================
    if opc == 1:
        cabeçalho('CADASTRAR NOVO LIVRO', 'sem cor', 'verde')

        # Captura dados do usuário já limpando espaços e padronizando texto
        livro = input('Nome do Livro: ').strip().title()
        autor = input('Nome do Autor: ').strip().title()

        # Chama função responsável por gravar no arquivo
        cadastrarLivro(arquivo, livro, autor)

    # ===================== OPÇÃO 2 — BUSCAR =====================
    elif opc == 2:
        cabeçalho('BUSCANDO LIVRO... ', 'sem cor', 'amarelo')

        # Recebe termo de busca
        proc = input('Buscar Livro: ').strip().title()

        # Executa busca no arquivo
        buscarLivro(arquivo, proc)

    # ===================== OPÇÃO 3 — EXCLUIR =====================
    elif opc == 3:
        cabeçalho('EXCLUSÃO DE LIVROS', 'sem cor', 'cinza')
        print('Qual livro deseja excluir?')

        # Mostra lista antes da exclusão
        linhaFina('cinza')
        listarLivros(arquivo)
        linhaFina('cinza')

        # Recebe índice do livro
        opc = leiaInt('Sua escolha: ')

        # Executa exclusão no arquivo
        excluirLivro(arquivo, opc)

    # ===================== OPÇÃO 4 — LISTAR =====================
    elif opc == 4:
        cabeçalho('LISTAGEM DE LIVROS', 'sem cor', 'azul')

        # Apenas exibe todos os livros
        listarLivros(arquivo)

    # ===================== OPÇÃO 5 — SAIR =====================
    else:
        # Mostra animação de encerramento
        encerrarPrograma()

        # Encerra o loop principal
        break