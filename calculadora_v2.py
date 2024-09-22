saida = '' 
def adicao(num1, num2):
    return  num1+num2
def subtracao(num1, num2):
    return  num1-num2
def multiplicacao(num1, num2):
    return  num1*num2
def divisao(num1, num2):
    if num2 == 0 :
        return "Não foi possível fazer a divisão por 0."
    else:
        return  num1/num2
def calculadora(num1, num2, operando):
    if (operando == "+") or ("adição" == str.lower(operando)):
        resultado = adicao(num1, num2)
    elif operando == "-" or "subtração" == str.lower(operando):
        resultado = subtracao(num1, num2)
    elif operando == "*" or "multiplicação" == str.lower(operando):
        resultado = multiplicacao(num1, num2)
    else:
        
        resultado = divisao(num1, num2)
    return resultado
while saida != "n":   
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    operando = input("Digite a operação: ")

    resultado = calculadora(num1, num2, operando)

    print(f"O resultado é: {resultado}")

    saida = input("Deseja continuar calculando ou sair? S/N ")
    saida = str.lower(saida)
print("Até logo")
    