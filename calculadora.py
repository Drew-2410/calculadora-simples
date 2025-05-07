def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

# Exemplo de uso
if __name__ == "__main__":
    print("Soma: ", somar(5, 3))
    print("Subtração: ", subtrair(5, 3))
    print("Multiplicação: ", multiplicar(5, 3))
    print("Divisão: ", dividir(5, 0))
