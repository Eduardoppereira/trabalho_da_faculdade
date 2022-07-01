# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no salário atual:
# o salários até R$ 280,00 (incluindo) : aumento de 20%
# o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o o salário antes do reajuste;
# o o percentual de aumento aplicado;
# o o valor do aumento;
# o o novo salário, após o aumento.

salario = float(input("Digite o seu salário"))

valor_baixo = salario * 0.20
baixo = salario * 1.20
valor_médio = salario * 0.15
medio = salario *1.15
valor_alto = salario *0.10
alto = salario * 1.10
valor_altissimo = salario * 0.05
altissimo = salario * 1.05

print ("Antes Reajuste: ", salario)

if salario <= 280: print("Aumento: 20%\nValor: ", valor_baixo, )
elif salario > 200 and salario <= 700: print ("Aumento: 15%\nValor: ", valor_médio, "\nFinal: ", medio)
elif salario > 700 and salario <= 1500: print ("Aumento: 10%\nValor: ", valor_alto, "\nFinal: ", alto)
else: print ("Aumento: 5%\nValor: ", valor_altissimo, "\nFinal: ", altissimo)