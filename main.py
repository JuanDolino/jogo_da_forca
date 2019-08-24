import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()

palavra = str(input("Digite a palavra a ser descoberta: ")).strip().lower()
letrasDescobertas = []
letrasEscritas = []
tentativas = 0
acertos = 0

for i in palavra:
    letrasDescobertas.append("_")

clear()

while True:
    if acertos == len(palavra):
        clear()
        print(f"Parabéns, você venceu !\n\nA palavra era {palavra}")
        break

    if tentativas == 5:
        print(f'Você perdeu !!\nA palavra certa era "{palavra}" ')
        break
    print(f"Letras já escritas: {letrasEscritas}\n\n")

    for i in letrasDescobertas:
        print(i, end=' ')

    print(f'\nTentativas: {tentativas}')
    palpite = str(input("Qual o seu palpite ?"))

    while palpite in letrasEscritas or len(palpite) > 1 or palpite.isdigit():
        if palpite in letrasEscritas:
        
            print("Essa letra já foi escrita, por favor tente novamente!")
            palpite = str(input("\n\nQual o seu palpite ?")) 
        
        if len(palpite) > 1:
            
            print("Por favor, escreva apenas uma letra")
            palpite = str(input("\n\nQual o seu palpite ?")) 

        if palpite.isdigit() == True:
        
            print("Isso não é uma letra, por favor digite apenas letras.")
            palpite = str(input("\n\nQual o seu palpite ?")) 

    letrasEscritas.append(palpite)
    palpite.lower()

    if palpite in palavra:
        if palavra.count(palpite) > 1:
            firstPositionPalpite = palavra.index(palpite)

            for i in range(0, palavra.count(palpite)+1):
                acertos+=1
                position = palavra[firstPositionPalpite:].index(palpite) + len(palavra[0:firstPositionPalpite])
                firstPositionPalpite+=1
                letrasDescobertas[position] = palpite
            acertos-=1
        else:
            acertos+=1
            letrasDescobertas[palavra.index(palpite)] = palpite
    else:
        tentativas+=1

    clear()