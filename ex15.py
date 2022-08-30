#15). Para o programa Python no arquivo ex15.py: 
# Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa. 
# No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. 
# O programa calculará quanto cada um deverá contribuir com a conta de energia.

valor_da_conta = float(input())
quantidade_de_pessoas = int(input())

valor_por_pessoa = valor_da_conta/quantidade_de_pessoas
print(valor_por_pessoa)