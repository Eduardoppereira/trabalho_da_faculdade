# Função 'valorPagamento' que calcula juros por dia de atraso e acrescenta multa em caso de atraso.
def valorPagamento(valor_da_prestação, numero_de_dias):
    juros = 0
    if numero_de_dias == 0:
        return valor_da_prestação
    else:
        juros = 0.1 * numero_de_dias

        return valor_da_prestação + ((3 * valor_da_prestação)/100) + juros 

total = 0
contador = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    contador += 1

print('Quantidade total: %d' % contador)
print('Valor total das prestações: %.2f' % total)