"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho, em metros quadrados, da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
"""

def main():
    tamanho = round(float(input("Digite quantos metros quadrados vão ser pintados: ")),2)
    litros_necessarios =  (tamanho/6) + (0.1*(tamanho/6))
    print("\nVão ser necessarios %.2f litros de tinta!"%litros_necessarios)
    informa_lata(litros_necessarios)
    informa_galoes(litros_necessarios)
    informa_mista(litros_necessarios)
    
#Função que informa ao usuario quantas latas ele pode comprar e o quanto ele vai gastar se só comprar latas
def informa_lata(litros_necessarios):
    lata = litros_necessarios/18
    if lata % 1 != 0:
        lata = lata - lata%1 + 1
    preço = lata*80
    print("\nCaso o usuario compre apenas latas, vai ter que comprar %i latas e gastar R$%i,00 reais."%(lata,preço))

#Função que informa ao usuario quantos galoes ele pode comprar e o quanto ele vai gastar se só comprar galoes
def informa_galoes(litros_necessarios):
    galao = litros_necessarios/4
    if galao % 1 != 0:
        galao = galao - galao%1 + 1
    preço = galao*25
    print("\nCaso o usuario compre apenas galões, vai ter que comprar %i galões e gastar R$%i,00 reais."%(galao,preço))

#Função que informa ao usuario a melhor opção de compra
def informa_mista(litros_necessarios):
    
    #Caso se necessite de uma quantidade de tinta de até 12 litros, vale mais a pena comprar apenas galoes.
    
    if litros_necessarios <= 12:
            galoes = litros_necessarios/4
            if galoes % 1 != 0:
                galoes = galoes - galoes%1 + 1
                gasto = galoes*25
            if galoes == 1:
                print("\nA melhor opção é comprar %i galão, o gasto será de R$%.2f."%(galoes,gasto))
            elif galoes > 1:
                print("\nA melhor opção é comprar %i galões, o gasto será de R$%.2f."%(galoes,gasto))
    else:
        
        #Caso se necessite de uma quantidade maior do que 12 litros, sempre vale mais a pena comprar o maximo de latas possíveis. 
        
        latas = litros_necessarios/18
        if latas % 1 != 0:
            latas = latas - latas%1
        litros_restantes = litros_necessarios - latas*18
        galoes = litros_restantes/4
        if galoes % 1 != 0:
            galoes = galoes - galoes%1 + 1
        gasto = galoes*25 + latas*80
        print("\nA melhor opção de compra é comprar %i latas e %i galões, tendo um gasto total de R$%i,00 reais."%(latas,galoes,gasto))
        
    
main()
