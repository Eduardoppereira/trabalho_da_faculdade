# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça: 
# o Mostre a quantidade de valores que foram lidos; check
# o Exiba todos os valores na ordem em que foram informados, um ao lado
# do outro;
# o Exiba todos os valores na ordem inversa à que foram informados, um
# abaixo do outro;
# o Calcule e mostre a soma dos valores;
# o Calcule e mostre a média dos valores;
# o Calcule e mostre a quantidade de valores acima da média calculada;
# o Calcule e mostre a quantidade de valores abaixo de sete;
# o Encerre o programa com uma mensagem;

num = cont = soma = 0
num = int(input("Digite um número:"))

lista = []

while num != -1:
    soma += num
    cont += 1
    num = int(input("Digite um número :"))

lista.append(num)

print("Quantidade de valores lidos: {}.".format(cont))
print("Soma dos valores: {}.".format(soma))

print (lista)



