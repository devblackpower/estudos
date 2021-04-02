from jogos.advinha import jogar_advinha
from jogos.forca import jogar_forca


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")


    jogo = int(input("Qual jogo?\n"))

    if jogo == 1:
        print("Jogando Forca")
        jogar_forca()
    elif jogo == 2:
        print("Jogando Advinhação")
        jogar_advinha()

if __name__ == '__main__':
    escolhe_jogo()