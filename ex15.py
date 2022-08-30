#15). Para o programa Python no arquivo ex15.py: 
# Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa. 
# No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. 
# O programa calculará quanto cada um deverá contribuir com a conta de energia.

valor_da_conta = float(input('Informe o valor da conta: '))
quantidade_de_pessoas = int(input('Informe a quantidade de moradores: '))

valor_por_pessoa = valor_da_conta/quantidade_de_pessoas
print(f'O valor a ser pago por cada morador é de R$ {valor_por_pessoa}')