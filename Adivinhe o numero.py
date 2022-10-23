import os
import random # Biblioteca para utilizar a função de sortear numeros aleatórios

os.system('cls')
print("ADIVINHE O NUMERO!\n")

jogador = input("Digite o seu nome: ")
jogadas = int(input("Digite um numero: "))
tentativas = 0 
numero_sorteado = random.randrange(0,50) # Permite sortear um numero aleatório, neste caso entre 0 e 50

# Loop para verificar se o numero sorteado corresponde ao numero digitado pelo usuário
while (numero_sorteado != jogadas):
    os.system('cls') # Vai limpar o conteudo do terminal e exibir a condição abaixo
    try:
        if (numero_sorteado > jogadas):
            print(f'Numero digitado: {jogadas}\nDigite um valor MAIOR' + '\n')
        elif (numero_sorteado < jogadas):
            print(f'Numero digitado: {jogadas}\nDigite um valor MENOR' + '\n')
        tentativas+=1
        jogadas = int(input("Digite um numero: "))
    except:
        if jogadas != int:
            print("\nApenas numeros sao validos!")
            exit("Fechando programa...\n")

print(f"\nParabens {jogador}! Voce acertou o numero sorteado '{numero_sorteado}' em {tentativas} tentativa(s)! \n")
os.system('pause'), os.system('cls')
