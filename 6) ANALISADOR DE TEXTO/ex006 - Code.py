from funcoes import *  # Importa todas as funções auxiliares do arquivo funcoes.py
from time import sleep  # Importa a função sleep para criar pausas no terminal

while True:  # Loop principal do programa (repete até o usuário escolher sair)
    sleep(1)  # Pausa de 1 segundo para efeito visual/organização da tela

    # Mostra o cabeçalho do sistema com estilização de cores
    cabeçalho('ANALISADOR DE TEXTO', 'amarelo', 'roxo')

    # Exibe o menu com as opções disponíveis
    menu(['ANALISAR TEXTO', 'SAIR'])

    # Lê a escolha do usuário garantindo que seja um número inteiro
    opc = leiaInt('Sua escolha: ')

    # Validação da opção — só aceita valores 1 ou 2
    while opc < 1 or opc > 2:
        print('\033[1;31m ERRO! Escolha uma opção válida.')  # Mensagem de erro em vermelho
        opc = leiaInt('Sua escolha: ')  # Pede novamente a opção

    # ================= OPÇÃO 1 — ANALISAR TEXTO =================
    if opc == 1:
        # Recebe o texto digitado, remove espaços extras e formata em Title Case
        texto = input('Digite o texto: ').strip().title()

        # Chama a função responsável por fazer a análise do texto
        analisarTexto(texto)

    # ================= OPÇÃO 2 — SAIR =================
    else:
        encerrarPrograma()  # Exibe mensagem/animação de encerramento
        break  # Sai do loop e finaliza o programa