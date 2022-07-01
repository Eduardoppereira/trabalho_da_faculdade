# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# o A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# o A mensagem "Reprovado", se a média for menor do que sete;
# o A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input ("Digite sua 1º nota:"))
nota2 = float(input ("Digite sua 2º nota:"))

nota_total = (nota1 + nota2) /2

if nota_total >= 7 and nota_total <10:
    print ("Você foi Aprovado! Parabéns!")

elif nota_total >= 10:
    print ("Você foi aprovado com excelência!!")

else:
    print ("Infelizmente você foi reprovado.")