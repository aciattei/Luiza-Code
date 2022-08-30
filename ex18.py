#18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro entre zero e 100. 
# Se o valor não estiver neste intervalo, informe que a nota é inválida. 
# Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário, informa que ele foi reprovado.

#18 Falta imprimir 'inválido' para float

nota_um = int(input())
#nota_dois = int(input())

if type(nota_um) == int:
  if nota_um >= 0 and nota_um <= 100:
    if nota_um >= 60:
      print('aprovado')
    if nota_um < 60:
          print('reprovado')
#  elif type(nota_um) == float:
#    print('nota inválida')
  else:
      print('nota inválida')