# Adivinhe-o-numero
Aplicação que roda diretamente no Terminal de forma interativa onde o usuário precisa adivinhar um numero sorteado aleatoriamente entre 0 e 50

# Tela inicial
```python
import os
import random # Biblioteca para utilizar a função de sortear numeros aleatórios

os.system('cls')
print("ADIVINHE O NUMERO!\n")

jogador = input("Digite o seu nome: ")
jogadas = int(input("Digite um numero: "))
tentativas = 0 
numero_sorteado = random.randrange(0,50) # Permite sortear um numero aleatório, neste caso entre 0 e 50
```
- Local onde o usuário vai indicar um nome e arriscar o primeiro numero

![image](https://user-images.githubusercontent.com/79271785/197419889-5fd4f6d6-786e-47da-8a0b-f3c0661cc8ae.png)


# Tela de interação
```python
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
```
- Aqui o usuário precisa seguir as instruções de 'Maior' e 'Menor' para adivinhar o numero que foi sorteado.  
MAIOR - o numero sorteado é maior que o ultimo numero digitado  
![image](https://user-images.githubusercontent.com/79271785/197419924-99982ab8-1085-46d1-ba47-c5d2b33a7350.png)  
MENOR - o numero sorteado é menor que o ultimo numero digitado  
![image](https://user-images.githubusercontent.com/79271785/197419978-c88a9a96-1447-4dc0-be89-65bc96a6f86e.png)

# Tela de Resultado
```python
print(f"\nParabens {jogador}! Voce acertou o numero sorteado '{numero_sorteado}' em {tentativas} tentativa(s)! \n")
os.system('pause'), os.system('cls')
```
- Quando o numero sorteado é descoberto, o sistema vai exibir uma mensagem indicando o nome do usuário, numero sorteado e a quantidade de tentativas  
![image](https://user-images.githubusercontent.com/79271785/197420113-002c8e07-37e7-4979-9f24-0d1c2a61043f.png)
