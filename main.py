'''
Jogo da Forca

Criador: Juan Vitor
Versão: v2.0

'''

import os
from time import sleep

#Função para executar a limpeza do terminal.

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()


palavra = str(input("Digite a palavra a ser descoberta: ")).strip().lower()
letrasDescobertas = []
letrasEscritas = []
tentativas = 0
acertos = -1

#Lista com o boneco em várias posições.

listaBoneco = [
    '''
    +---------+
    |         |
    |
    |
    |
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |
    |
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |         |
    |
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |        /|
    |
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |        /|\\
    |
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |        /|\\
    |        /
    ======

    ''',
    '''
    +---------+
    |         |
    |         0
    |        /|\\
    |        / \\
    ======

    '''

    
]


for i in palavra:
    letrasDescobertas.append("_")

clear()

while acertos != len(palavra) or tentativas != 6:
    if acertos == len(palavra):
        clear()
        print(f"Parabéns, você venceu !\n\nA palavra era {palavra}")
        break

    if tentativas == 6:
        print(listaBoneco[tentativas])

        print(f'\nVocê perdeu !!\nA palavra certa era "{palavra}" ')
        sleep(1)
        break
    print(f"Letras já escritas: {letrasEscritas}\n\n")

    print(f"\n\n{listaBoneco[tentativas]}\n\n")

    for i in letrasDescobertas:
        print(i, end=' ')

    palpite = str(input("\nQual o seu palpite ?")).strip()

    # While criado para evitar erros

    while palpite in letrasEscritas or len(palpite) > 1 or len(palpite) == 0 or palpite.isdigit():
        if palpite in letrasEscritas:
        
            print("Essa letra já foi escrita, por favor tente novamente!")
            palpite = str(input("\n\nQual o seu palpite ?")) 
        
        if len(palpite) > 1 or len(palpite) == 0:
            
            print("Por favor, escreva apenas uma letra")
            palpite = str(input("\n\nQual o seu palpite ?")) 

        if palpite.isdigit() == True:
        
            print("Isso não é uma letra, por favor digite apenas letras.")
            palpite = str(input("\n\nQual o seu palpite ?")) 

    letrasEscritas.append(palpite)
    palpite.lower()

    if palpite in palavra:
        if palavra.count(palpite) > 1:
            positionPalpite = palavra.index(palpite)

            for i in range(0, palavra.count(palpite)+1):
                
                # A váriavel position primeiro procura a posição do palpite da pessoa na lista
                # Quando ele achar a posição ele vai somar com o tamanho da lista, de 0 ate a posição do palpite

                position = palavra[positionPalpite:].index(palpite) + len(palavra[0:positionPalpite])
                
                # Aqui ele adiciona mais 1 a variavel positionPalpite, para que ele procure a próxima posição.
                
                positionPalpite+=1
                
                # Adiciona o palpite a lista.

                letrasDescobertas[position] = palpite
                acertos+=1

        else:
            acertos+=1
            letrasDescobertas[palavra.index(palpite)] = palpite
    else:
        tentativas+=1

    clear()