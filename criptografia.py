def lin():
    print('-' * 30)


lin()
print('PROGRAMA DE CRIPTOGRAFIA')
lin()

def criptografar(texto, chave):
    TextoInserido = ""  # Define essa variável como string

    for caractere in texto:
        if caractere.isalpha():
            maiuscula = caractere.isupper()
            caractere = caractere.lower()

            # Realiza a extração Unicode
            codigo = ord(caractere)
            codigo_criptografado = ((codigo - 97 + chave) % 26) + 97

            # Condição de inserção
            if maiuscula:
                TextoInserido += chr(codigo_criptografado).upper()
            else:
                TextoInserido += chr(codigo_criptografado)

        else:
            TextoInserido += caractere

    return TextoInserido

def descriptografar(texto, chave):  # Função para descriptografar o texto
    return criptografar(texto, -chave)

def main():
    mensagem = input("Digite a mensagem que você deseja criptografar: ")

    # Verificação da chave de criptografia
    while True:
        chave = int(input("Digite a chave (1 a 26): "))
        if 1 <= chave <= 26:
            break
        print("A chave deve estar entre 1 e 26. Tente novamente.")

    mensagem_criptografada = criptografar(mensagem, chave)  # Define a mensagem criptografada nessa variável

    lin()
    print("Mensagem criptografada:", mensagem_criptografada)

    descriptografar_opcao = input("Deseja descriptografar a mensagem? (S/N): ")

    if descriptografar_opcao.upper() == 'S':
        while True:
            chave_descriptografar = int(input("Digite a chave para descriptografar: "))
            
            # Verifica se a chave de descriptografia está correta
            if chave_descriptografar == chave:
                mensagem_descriptografada = descriptografar(mensagem_criptografada, chave_descriptografar)
                print("-------------------- Chave liberada --------------------\n")
                print("Mensagem descriptografada:", mensagem_descriptografada, "\n")
                lin()
                break
            else:
                print("Chave incorreta. Tente novamente.")
    else:
        print("\n------------ Obrigada por utilizar a criptografia --------------")

if __name__ == "__main__":
    main()
