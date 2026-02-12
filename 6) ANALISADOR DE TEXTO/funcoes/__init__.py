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

def analisarTexto(text):
    # String que armazenará apenas letras, números e espaços do texto original
    new_texto = ''

    # Listas para armazenar separadamente cada tipo de caractere
    letras = []
    numeros = []
    caracs = []

    # Percorre cada caractere digitado no texto
    for i in text:
        if i.isalpha():  # Se o caractere for uma letra
            letras.append(i)  # adiciona na lista de letras
            new_texto += i  # adiciona também no novo texto

        elif i == ' ':  # Se for espaço
            new_texto += i  # mantém o espaço no novo texto

        elif i.isnumeric():  # Se for número
            new_texto += i  # adiciona o número no novo texto
            numeros.append(i)  # guarda o número na lista de números

        else:  # Qualquer outro caractere (pontuação, símbolos etc.)
            caracs.append(i)  # guarda na lista de caracteres especiais

    # Divide o texto em palavras, ignorando múltiplos espaços
    lista_texto = new_texto.split()

    # Percorre a lista de palavras para descobrir a maior e a menor
    for pos, i in enumerate(lista_texto):
        if pos == 0:  # Na primeira palavra, ela é ao mesmo tempo maior e menor
            maior = i
            menor = i
        else:
            # Verifica se a palavra atual é maior que a maior registrada
            if len(i) > len(maior):
                maior = i

            # Verifica se a palavra atual é menor que a menor registrada
            if len(i) < len(menor):
                menor = i

    # --- Impressão do relatório visual ---

    linhaGrossa('azul')  # Linha decorativa grossa
    print('RELATÓRIO'.center(72))  # Título centralizado
    linhaGrossa('azul')
    sleep(0.7)  # Pequena pausa para efeito visual

    # Quantidade de palavras
    print(f'Quantidade de palavras digitadas: {len(lista_texto)}')
    sleep(0.7)

    linhaFina('azul')
    # Quantidade de letras
    print(f'Quantidade de letras digitadas: {len(letras)}')
    sleep(0.7)

    linhaFina('azul')
    # Quantidade de números
    print(f'Quantidade de números digitados: {len(numeros)}')
    sleep(0.7)

    # Quantidade de caracteres especiais
    print(f'Quantidade de caracteres especiais digitados {len(caracs)}')
    sleep(0.7)

    linhaFina('azul')
    # Maior palavra encontrada
    print(f'Maior palavra digitada: {maior}')
    sleep(0.7)

    linhaFina('azul')
    # Menor palavra encontrada
    print(f'Menor palavra digitada: {menor}')
    sleep(0.3)

#####################################################################################################################
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