"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
	notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
	três notas de 100, uma nota de 50, quatro notas de 10,
	uma nota de 5 e quatro notas de 1.

"""

def main():
    valor_saque = saque()
    notas_usadas = notas(valor_saque)
    forma_frase(notas_usadas, valor_saque)

#Função que define o quanto o usuario vai sacar
def saque():
    valor = int(input("Digite quanto vai ser sacado: "))
    while True:
        if valor < 10:
            print("\nO valor mínimo para saques é de R$10,00!")
            valor = int(input("\nDigite quanto vai ser sacado:"))
        elif valor > 600:
            print("\nO valor máximo para saques é de R$600,00!:" )
            valor = int(input("\nDigite quanto vai ser sacador:"))
        else:
            break
    return valor

#Função que define as notas que o usuario vai pegar
def notas(valor_saque):
    notas_100 = valor_saque//100
    notas_50 = (valor_saque%100)//50
    notas_10 = (valor_saque - 100*notas_100 - 50*notas_50)//10
    notas_5 = (valor_saque - 100*notas_100 - 50*notas_50 - 10*notas_10)//5
    notas_1 = (valor_saque - 100*notas_100 - 50*notas_50 - 10*notas_10)%5
    lista_notas = [[100,notas_100],[50, notas_50],[10, notas_10], [5,notas_5],[1, notas_1]]
    return lista_notas

#Função que printa a quantidade de notas utilizadas
def forma_frase(notas_usadas, valor_saque):
    plural = [0,1,' duas notas de',' três notas de',' quatro notas de',' cinco notas de',' seis notas de']
    singular = [' nenhuma nota de',' uma nota de']
    frase = '\nPara sacar o valor de ' +str(valor_saque)+' foram necessarias, '
    for i in notas_usadas:
        if i[1] <= 1:
            if i[0] == 1:
                frase += 'e '+ str(singular[i[1]]) + ' ' + str(i[0]) + '.'
            else:
                frase += str(singular[i[1]]) + ' ' + str(i[0]) + ','
        else:
            if i[0] == 1:
                frase += 'e ' + str(plural[i[1]]) + ' ' + str(i[0]) + '.'
            else:
                frase += str(plural[i[1]]) + ' ' + str(i[0]) + ','
    print(frase)
main()
