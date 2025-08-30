print("~~~~~~~~~~~~~~~~~~")
pontos = float(input("Digite os pontos obtidos: "))

if pontos >= 0 and pontos <= 30:
    print("Regular")
    print("~~~~~~~~~~~~~~~~~~~")
elif pontos >= 31 and pontos <= 60:
    print("Bom")
    print("~~~~~~~~~~~~~~~~~~~")
elif pontos >= 61 and pontos <= 90:
    print("Muito bom")
    print("~~~~~~~~~~~~~~~~~~~~")
elif pontos >= 91 and pontos <= 100:
    print("Ótimo")
    print("~~~~~~~~~~~~~~~~~~~~~")
else:
    print("Pontuação Inválida")
    print("~~~~~~~~~~~~~~~~~~~~~")