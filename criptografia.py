def lin():
    print('-'*30)


lin()
print('PROGRAMA DE CRIPTOGRAFIA')
lin()

def criptografar(texto, chave):

    TextoInserido = "" #Define essa variável como string

    for caractere in texto:
        if caractere.isalpha():

            maiuscula = caractere.isupper()
            caractere = caractere.lower()    

            #Essas duas linhas, realizam a extração Unicode 
            codigo = ord(caractere)
            codigo_criptografado = ((codigo - 97 + chave) % 26) + 97


            #condição de inserção
            if maiuscula:
                TextoInserido += chr(codigo_criptografado).upper()
            else:
                TextoInserido += chr(codigo_criptografado)

        else:
            TextoInserido += caractere

    return TextoInserido


def descriptografar(texto, chave):   # Função para descriptografar o texto
    
    return criptografar(texto, -chave)

def main():

    mensagem = input("Digite a mensagem que voce deseja criptografar: ")  
    chave = int(input("Digite a chave: "))

    mensagem_criptografada = criptografar(mensagem, chave)  #Define a mensagem criptografada nessa variável
    
    lin()
    print("Mensagem criptografada:", mensagem_criptografada)
    

    descriptografar_opcao = input("Deseja descriptografar a mensagem? (S/N): ")
    
    if descriptografar_opcao.upper() == 'S':

        chave_descriptografar = int(input("Digite a chave para descriptografar: \n"))

        mensagem_descriptografada = descriptografar(mensagem_criptografada, chave_descriptografar)

        print("--------------------Chave liberada-------------------- \n")
        print("Mensagem descriptografada:", mensagem_descriptografada, "\n")
        lin()
 
    else:
        print("\n------------Obrigada por utilizar a criptografia--------------")

if __name__ == "__main__":
    main()



