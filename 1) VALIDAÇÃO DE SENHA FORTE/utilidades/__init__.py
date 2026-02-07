def validaSenha(senha):
  # Loop infinito até a senha ser válida
  while True:
    # Verifica tamanho mínimo
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

    # Solicita nova senha caso tenha erro
    senha = input("Digite novamente: ").strip().lower()


def existeNum(text):
  # Flag para indicar se encontrou número
  tem_num = False

  # Percorre cada caractere do texto
  for i in text:
    if i.isdigit():   # Verifica se é dígito
      tem_num = True
      break           # Para o loop ao encontrar

  return tem_num      # Retorna True ou False


def existeLetra(senha):
  # Flag para indicar se encontrou letra
  tem_letra = False

  # Percorre cada caractere da senha
  for i in senha:
    if i.isalpha():   # Verifica se é letra
      tem_letra = True
      break           # Para o loop ao encontrar

  return tem_letra    # Retorna True ou False