# Importa todas as funções do arquivo funcoes.py
from funcoes import *

# Define o nome do arquivo onde os contatos serão armazenados
arquivo = 'contatos.txt'

# Verifica se o arquivo existe; se não existir, cria o arquivo
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

# Loop principal do programa (roda até o usuário escolher encerrar)
while True:
    sleep(2)  # Pausa de 2 segundos para melhor experiência visual

    # Exibe o cabeçalho principal do sistema
    cabeçalho('AGENDA DE CONTATOS', 'roxo')

    # Mostra o menu de opções para o usuário
    menu(['CADASTRAR CONTATO', 'VER CONTATOS', 'ALTERAR CONTATO', 'EXCLUIR CONTATO', 'ENCERRAR'])

    # Lê a opção escolhida pelo usuário garantindo que seja um inteiro
    escolha = leiaInt('Sua escolha: ')

    # Validação: mantém o usuário no loop até escolher uma opção válida (1 a 5)
    while escolha > 5 or escolha < 1:
        print('\033[31mERRO! Escolha uma opção válida.\033[m')
        escolha = leiaInt('Sua escolha: ')

    # ================= CADASTRAR CONTATO =================
    if escolha == 1:
        sleep(1)
        cabeçalho('NOVO CONTATO', 'verde')

        # Coleta e trata os dados do contato
        nome = input('Nome: ').strip().title()
        tel = leiaInt('Telefone: ')
        email = input('E-mail: ').strip()

        # Salva o contato no arquivo
        cadastrarContato(arquivo, nome, tel, email)

    # ================= VER CONTATOS =================
    elif escolha == 2:
        sleep(1)
        cabeçalho('LISTA DE CONTATOS', 'azul')

        # Imprime o cabeçalho da tabela de contatos
        print(f'{'         NOME':<15}{'      TELEFONE':<12}{'       E-MAIL':<20}')
        print('-' * 64)

        # Mostra todos os contatos salvos no arquivo
        mostrarContatos(arquivo)

    # ================= ALTERAR CONTATO =================
    elif escolha == 3:
        sleep(1)
        cabeçalho('ALTERAR CONTATO', 'amarelo')
        print('\033[1mQual contato deseja alterar?\033[m')

        # Exibe lista de contatos para o usuário escolher
        mostrarContatos(arquivo)

        # Lê o índice/opção do contato a ser alterado
        opc = leiaInt('Sua opção: ')

        # Executa a alteração do contato
        alterarContato(arquivo, opc)

    # ================= EXCLUIR CONTATO =================
    elif escolha == 4:
        sleep(1)
        cabeçalho('EXCLUIR CONTATO', 'vermelho')
        print('\033[1mQual contato deseja excluir?\033[m')

        # Mostra os contatos disponíveis
        mostrarContatos(arquivo)

        # Lê o índice do contato a ser removido
        opc = leiaInt('Sua opção: ')

        # Remove o contato do arquivo
        excluirContato(arquivo, opc)

    # ================= ENCERRAR =================
    else:
        # Chama função de encerramento (mensagem final, limpeza, etc.)
        encerrarPrograma()
        break  # Sai do loop principal e finaliza o programa
