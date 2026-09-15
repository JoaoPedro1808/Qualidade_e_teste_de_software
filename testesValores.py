import random as rmd

def valoresInicias():
    print("Valores inicias")
    valorMax = int(input("Digite o valor maximo: "))
    valorMin = int(input("Digite o valor minimo: "))

    return valorMax, valorMin

def telaInicial():
    maximo, minimo = valoresInicias()

    escolherTeste(maximo, minimo)

def testeValoresLimites(valorMax, valorMin):
    print("Teste de valores limites")

    bordainferior = valorMin - 1
    bordaSuperior = valorMax + 1

    print(f"Limite superior: {valorMax} || VALIDO")
    print(f"Limite inferior: {valorMin} || VALIDO")
    print(f"Bordar superior: {bordaSuperior} || INVALIDO")
    print(f"Bordar inferior: {bordainferior} || INVALIDO")

def testesValoresEquivalentes(valorMax, valorMin):
    print("Teste de valores equivalentes")

    invalidoInferior = rmd.randint(valorMin - 50, valorMin - 1)
    valido = rmd.randint(valorMin, valorMax)
    invalidoSuperior = rmd.randint(valorMax + 1, valorMax + 50)

    print(f"Menor que {valorMin}: {invalidoInferior} || INVALIDO")
    print(f"Entre os dois: {valido} || VALIDO")
    print(f"Maior que {valorMax}: {invalidoSuperior} || INVALIDO")

def escolherTeste(valorMax, valorMin):
    print("Escolha um teste (digitando um numero)")
    print("1. Teste de valor limite")
    print("2. Teste valor equivalente")

    escolha = int(input("Digite a opção (1 ou 2): "))

    if escolha == 1:
        testeValoresLimites(valorMax, valorMin)
    elif escolha == 2:
        testesValoresEquivalentes(valorMax, valorMin)
    else:
        print("Opção invalida")

telaInicial()