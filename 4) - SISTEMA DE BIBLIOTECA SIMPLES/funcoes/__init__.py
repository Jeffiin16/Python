# Importa a função sleep para criar pequenas pausas no terminal
from time import sleep

# Dicionário com códigos ANSI para cores no terminal
# Facilita reaproveitar cores sem repetir códigos mágicos no código
cores = {
    'sem cor': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'cinza': '\033[1;36m'
}

######################################################################################################################

# Imprime uma linha fina decorativa no terminal
# Parâmetro opcional permite escolher a cor
def linhaFina(cor='sem cor'):
    print(f'{cores[cor]}-\033[m' * 72)

# Imprime uma linha grossa decorativa no terminal
def linhaGrossa(cor='sem cor'):
    print(f'{cores[cor]}▬\033[m' * 45)

#######################################################################################################################

# Exibe um menu enumerado com base em uma lista de opções
def menu(lista):
    for pos, i in enumerate(lista, start=1):
        print(f'\033[1m[ {pos} ] - {i}\033[m')

######################################################################################################################

# Mostra um cabeçalho formatado com linhas e cores
# texto = título
# cor_texto = cor da fonte
# cor_linha = cor das linhas decorativas
def cabeçalho(texto, cor_texto, cor_linha):
    linhaGrossa(cor_linha)
    print(f'{cores[cor_texto]}{texto.center(72)}\033[m')
    linhaGrossa(cor_linha)

#####################################################################################################################

# Verifica se o arquivo existe
# Retorna True se existir, False se não existir
def arquivoExiste(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

#####################################################################################################################

# Cria o arquivo caso ele não exista
def criarArquivo(arquivo):
    try:
        arq = open(arquivo, 'wt+')
        arq.close()
    except:
        print(f'Não foi possível criar o arquivo {arquivo}.')
    else:
        print(f'arquivo \033[4m{arquivo}\033[m criado com sucesso!')

#######################################################################################################################

# Lê um número inteiro do usuário com tratamento de erro
# Garante que o programa não quebre se o usuário digitar texto
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        else:
            return num

#######################################################################################################################

# Cadastra um livro no arquivo
# Valida campos vazios e evita duplicidade
def cadastrarLivro(arquivo, nome, autor):
    try:
        arq = open(arquivo, 'rt')
        lista  = arq.readlines()
        arq.close()
    except:
        print(f'Não foi possível abrir o arquivo {arquivo}.')
    else:
        # Validação de campos vazios
        while True:
            if nome == '':
                print('\033[1;33mPor favor, preencha o NOME do livro.\033[m')
                nome = input('Nome do livro: ').strip().title()
            if autor == '':
                print('\033[1;33mPor favor, preencha o AUTOR do livro.\033[m')
                autor = input('Autor do livro: ').strip().title()
            if nome != '' and autor != '':
                break

        cadastrado = False

        # Verifica duplicidade comparando apenas o nome do livro
        for i in lista:
            if nome == i.split(';')[0]:
                print(f'O livro {nome} já está cadastrado!\033[m')
                cadastrado = True
                break

        # Se não estiver cadastrado, adiciona no final do arquivo
        if not cadastrado:
            try:
                arq = open(arquivo, 'at')
            except:
                print(f'Não foi possível cadastrar o livro {nome}.')
            else:
                arq.writelines(f'{nome};{autor}\n')
                arq.close()
                print(f'O livro \033[1;32m{nome}\033[m foi cadastrado com sucesso!')

#######################################################################################################################

# Busca livros pelo nome (busca parcial)
def buscarLivro(arquivo, livro):
    try:
        arq = open(arquivo, 'rt')
        lista = arq.readlines()
        arq.close()
    except:
        print(f'Não foi possível abrir o arquivo {arquivo}.')
    else:
        nova_lista = []

        # Percorre os livros e verifica se o termo está no título
        for i in lista:
            i = i.split(';')
            if livro in i[0]:
                nova_lista.append(i[0])

        # Exibe resultado
        if len(nova_lista) == 0:
            print('Nenhum livro encontrado')
        else:
            linhaFina()
            print('LIVROS ENCONTRADOS')
            linhaFina()
            for pos, item in enumerate(nova_lista, start=1):
                print(f'[ {pos} ] - {item}')
            linhaFina()

######################################################################################################################

# Lista todos os livros formatados em tabela
def listarLivros(arquivo):
    try:
        arq = open(arquivo, 'rt')
        lista = arq.readlines()
        arq.close()
    except:
        print(f'Não foi possível abrir o arquivo {arquivo}.')
    else:
        nova_lista = []

        # Organiza dados separando título e autor
        for i in lista:
            i = i.split(';')
            i[1] = i[1].replace('\n', '')
            nova_lista.append(i)

        # Cabeçalho da tabela
        print(f'{"":<10}{"Livro":<35}{"Autor"}')
        linhaFina()

        # Exibe linha a linha com efeito visual
        for posicao, item in enumerate(nova_lista, start=1):
            print(f'\033[7m[ {posicao} ] - {item[0]:<30}{item[1]:<34}\033[m')
            sleep(0.4)

######################################################################################################################

# Exclui um livro pelo índice
def excluirLivro(arquivo, escolha):
    try:
        arq = open(arquivo, 'rt')
        lista = arq.readlines()
        arq.close()
    except:
        print(f'Não foi possível abrir o arquivo {arquivo}.')
    else:
        # Validação do índice escolhido
        while escolha < 1 or escolha > len(lista):
            print('\033[1;31mERRO! Escolha uma opção válida.\033[m')
            escolha = leiaInt('Sua opção: ')

        nova_lista = []
        x = []

        # Reconstrói lista sem o item removido
        for pos, i in enumerate(lista, start=1):
            if pos != escolha:
                nova_lista.append(i)
            else:
                x = i.split(';')

        # Sobrescreve o arquivo sem o livro removido
        try:
            arq = open(arquivo, 'wt')
        except:
            print(f'Não foi possível excluir o livro {x[0].upper()}')
        else:
            arq.writelines(nova_lista)
            arq.close()
            print(f'O livro \033[1;34m{x[0].upper()}\033[m foi excluido com sucesso!')

#######################################################################################################################

# Mensagem e efeito visual de encerramento do programa
def encerrarPrograma():
    linhaGrossa('vermelho')
    print(f'                     \033[1;31mENCERRANDO PROGRAMA',end='')
    sleep(0.7)
    print('.',end='')
    sleep(0.7)
    print('.', end='')
    sleep(0.7)
    print('.\033[m')
    sleep(0.4)
    print('\033[1;41mATÉ A PRÓXIMA!\033[m'.center(72))
    linhaGrossa('vermelho')