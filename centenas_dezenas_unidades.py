"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


def main():
    numero = numero_escolhido()
    centena = numero//100
    dezena = (numero%100)//10
    unidade = numero - centena*100 - dezena*10
    frase = str(numero) + ' = ' + ' '
    if centena == 1:
        frase += str(centena)+' centena, '
    else:
        frase += str(centena)+' centenas, '
    if dezena == 1:
        frase += str(dezena)+' dezena e '
    else:
        frase += str(dezena)+' dezenas e '
    if unidade == 1:
        frase += str(centena)+' unidade.'
    else:
        frase += str(centena)+' unidades.'
    print(frase)

#Função na qual o usuario escolhe um número menor do que 1000
def numero_escolhido():
    numero = int(input("Digite um número menor do que 1000:"))
    while True:
        if numero < 0:
            numero *= -1
        if numero >= 1000:
            print("\nEntrada invalida! O número deve, em módulo, deve ser menor do que 1000!")
            numero = int(input("Digite um número menor do que 1000:"))
        else:
            break
    return numero
 
main()            
