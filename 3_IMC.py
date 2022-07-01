# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58 - Para mulheres: (62.1*h) - 44.7


sexo = input("Qual teu sexo? Masculino (M) ou Feminino (F)?")
altura = input('Digite tua altura')

peso_ideal_m = (72.7 * float(altura)) - 58
peso_ideal_f = (62.1 * float(altura)) - 44.7

if sexo == "M":
    print("Teu peso ideal é %.2f: " % peso_ideal_m)

elif sexo == "F":
    print("Teu peso ideal é %.2f:" % peso_ideal_f)

else:
    print("Sexo invalido!")