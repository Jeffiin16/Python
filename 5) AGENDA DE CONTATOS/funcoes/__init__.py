from time import sleep  # Importa função para criar pausas no terminal

# Dicionário com linhas coloridas usando código ANSI
cores = {
    'vermelho': '\033[1;31m▬\033[m' * 40,
    'verde': '\033[1;32m▬\033[m' * 40,
    'amarelo': '\033[1;33m▬\033[m' * 40,
    'azul': '\033[1;34m▬\033[m' * 40,
    'roxo': '\033[1;35m▬\033[m' * 40,
    'cinza': '\033[1;36m▬\033[m' * 40,
    'sem cor': '\033[m▬\033[m' * 40
}

def linha(cor='sem cor'):
    print(f'{cores[cor]}')  # Imprime uma linha decorativa na cor escolhida

# ======================================================================

def cabeçalho(texto, cor='sem cor'):
    linha(cor)  # Linha superior
    print(f'\033[1m{texto.center(60)}\033[m')  # Texto centralizado e em negrito
    linha(cor)  # Linha inferior

# ======================================================================

def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')  # Tenta abrir o arquivo em modo leitura
        arq.close()
    except FileNotFoundError:  # Se não encontrar o arquivo
        return False
    else:
        return True  # Arquivo existe

# ======================================================================

def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')  # Cria o arquivo caso não exista
        arq.close()
    except:
        print(f'Não foi possível criar o arquivo {nome}.')  # Mensagem de erro
    else:
        print(f'Arquivo \033[4m{nome}\033[m criado com sucesso!')  # Mensagem de sucesso

# ======================================================================

def cadastrarContato(arquivo, nome, tel, email):
    try:
        arq = open(arquivo, 'at')  # Abre o arquivo para adicionar conteúdo
    except:
        print('Erro ao abrir o arquivo.')
    else:
        arq.writelines(f'{nome};{tel};{email}\n')  # Salva contato separado por ;
        arq.close()
        print(f'Contato cadastrado com sucesso!')

# ======================================================================

def mostrarContatos(arquivo):
    try:
        arq = open(arquivo, 'rt')  # Abre arquivo para leitura
        linha = arq.readlines()  # Lê todas as linhas
        arq.close()
    except:
        print('Erro ao ler o arquivo.')
    else:
        nova_lista = []  # Lista auxiliar para organizar dados

        for pos, i in enumerate(linha):
            nova_lista.append(i.split(';'))  # Divide nome;tel;email
            nova_lista[pos][2] = nova_lista[pos][2].replace('\n', '')  # Remove quebra de linha

        for pos, item in enumerate(nova_lista, start=1):
            # Exibe contato formatado e numerado
            print(f'\033[7;30m[ {pos} ] - {item[0]:<10}| {item[1]:<12}| {item[2]:<20}\033[m')
            sleep(0.4)  # Pausa para efeito visual

# ======================================================================

def alterarContato(arquivo, escolha):
    try:
        arq = open(arquivo, 'rt')  # Lê o arquivo
        linha = arq.readlines()
        arq.close()
    except:
        print('Não foi possivel abrir o arquivo.')
    else:
        nova_lista = []

        # Valida escolha do usuário
        while escolha < 1 or escolha > len(linha):
            print('\033[31mERRO! Escolha uma opção válida.\033[m')
            escolha = leiaInt('Sua opção: ')

        # Coleta novos dados
        nome = input('Nome: ').strip().title()
        tel = leiaInt('Telefone: ')
        email = input('E-mail: ').strip()

        # Reconstrói lista substituindo apenas o contato escolhido
        for pos, i in enumerate(linha, start=1):
            if pos == escolha:
                nova_lista.append(f'{nome};{tel};{email}\n')
            else:
                nova_lista.append(i)

        try:
            arq = open(arquivo, 'wt')  # Reescreve o arquivo
            arq.writelines(nova_lista)
        except:
            print('Não foi possível alterar o contato.')
        else:
            arq.close()
            print(f'\033[1;35mContato alterado com sucesso!\033[m')

# ======================================================================

def excluirContato(arquivo, escolha):
    try:
        arq = open(arquivo, 'rt')  # Lê o arquivo
        linha = arq.readlines()
        arq.close()
    except:
        print('Não foi possivel abrir o arquivo.')
    else:
        # Validação da escolha
        while escolha < 1 or escolha > len(linha):
            print('\033[31mERRO! Escolha uma opção válida.\033[m')
            escolha = leiaInt('Sua opção: ')

        nova_lista = []

        # Mantém apenas os contatos diferentes do escolhido
        for pos, i in enumerate(linha, start=1):
            if pos != escolha:
                nova_lista.append(i)

        try:
            arq = open(arquivo, 'wt')  # Reescreve sem o contato excluído
            arq.writelines(nova_lista)
        except:
            print('Não foi possível excluir o contato.')
        else:
            arq.close()
            print(f'\033[1;35mContato excluido com sucesso!\033[m')

# ======================================================================

def menu(lista):
    # Exibe opções numeradas dinamicamente
    for pos, i in enumerate(lista, start=1):
        print(f'[ {pos} ] - {i}')

# ======================================================================

def leiaInt(msg):
    while True:  # Loop até digitar número válido
        try:
            num = int(input(msg))  # Converte para inteiro
        except (TypeError, ValueError):
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
            continue  # Volta ao início do loop
        else:
            return num  # Retorna número válido
            break  # Nunca será executado (desnecessário)

# ======================================================================

def encerrarPrograma():
    linha('cinza')  # Linha decorativa
    print('                  Encerrando o programa', end='')
    sleep(1)
    print('\033[1;31m.', end='')  # Pontos animados
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.\033[m')
    sleep(0.5)
    print(f'\033[1;31m{"PROGRAMA ENCERRADO!".center(60)}\033[m')  # Mensagem final
    linha('cinza')