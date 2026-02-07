def validaSenha(senha):
  # Loop infinito até a senha atender todos os critérios
  while True:
    # Verifica se tem no mínimo 8 caracteres
    if len(senha) < 8:
        print("\033[1;35mERRO! A senha precisa ter 8 caracteres\033[m")

    # Verifica se possui número
    elif not existeNum(senha):
        print("\033[1;35mERRO! A senha precisa ter números\033[m")

    # Verifica se possui letra
    elif not existeLetra(senha):
        print("\033[1;35mERRO! A senha precisa ter letras\033[m")

    # Se passou em todas as validações
    else:
        return "\033[1;33mSENHA VÁLIDA!\033[m"

    # Solicita nova senha se houver erro
    senha = input("Digite novamente: ").strip().lower()


def existeNum(text):
  # Indica se encontrou número
  tem_num = False

  # Percorre cada caractere do texto
  for i in text:
    if i.isdigit():   # Verifica se é dígito
      tem_num = True
      break           # Interrompe ao encontrar

  return tem_num      # Retorna True ou False


def existeLetra(senha):
  # Indica se encontrou letra
  tem_letra = False

  # Percorre cada caractere da senha
  for i in senha:
    if i.isalpha():   # Verifica se é letra
      tem_letra = True
      break           # Interrompe ao encontrar

  return tem_letra    # Retorna True ou False


def leiaFloat(msg=''):
  # Lê entrada do usuário
  num = input(msg).strip()

  while True:
    # Impede valor começando com ponto
    if num[0] == '.':
      print(f'\033[1;32mERRO! Digite um valor válido para a nota.\033[m')
      num = input(msg)

    # Verifica número com ponto
    if num.replace('.', '').isnumeric():
      num = float(num)
      break

    # Verifica número com vírgula
    elif num.replace(',', '').isnumeric():
      num = float(num.replace(',', '.'))
      break

    # Caso inválido
    else:
      print(f'\033[1;32mERRO! Digite um valor válido para a nota.\033[m')
      num = input(msg)

  return num  # Retorna o valor float validado