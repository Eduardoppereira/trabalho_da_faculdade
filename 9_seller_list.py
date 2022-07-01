#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
#vendedores com base em comissões. O vendedor recebe $200 por semana
#mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
#vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais
#9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
#um array de contadores) que determine quantos vendedores receberam
#salários nos seguintes intervalos de valores:
#o $200 - $299
#o $300 - $399
#o $400 - $499
#o $500 - $599
#o $600 - $699
#o $700 - $799
#o $800 - $899
#o $900 - $999
#o $1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
#sem fazer vários ifs aninhados.


def valorPagamento(valor, dias):
    juros = 0
    if dias == 0:
        return valor
    else:
        juros = 0.1 * dias

        return valor + ((3 * valor)/100) + juros 

total = 0
cont = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    cont += 1

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)