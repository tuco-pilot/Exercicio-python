"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)

EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>>
"""

def main():
    numero_1 = round(float(input("Digite o primeiro número: ")),2)
    numero_2 = round(float(input("Digite o segundo número: ")),2)
    resultado = [str(numero_1) + ' + ' + str(numero_2) + ' = ' + str(numero_1 + numero_2), str(numero_1) + ' - ' + str(numero_2) + ' = ' + str(numero_1 - numero_2),
                 str(numero_1) + ' x ' + str(numero_2) + ' = ' + str(numero_1 * numero_2), str(numero_1) + ' / ' + str(numero_2) + ' = ' + str(round(numero_1 / numero_2,2)),
                 str(numero_1) + ' // '+ str(numero_2) + ' = ' + str(numero_1 // numero_2),str(numero_1) + ' % ' + str(numero_2) + ' = ' + str(round(numero_1 % numero_2,2))]
    print("Numero 1 = %i \nNumero 2 = %i"%(numero_1,numero_2))
    for i in resultado:
        print(i)
    
    
main()
