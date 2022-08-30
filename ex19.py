#19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for … 
# ● menor que R$1000,00, o vendedor não ganha nenhuma comissão; 
# ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da venda; 
# ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda; 
# ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda; 
# ● acima de R$50.000,00 a comissão será de 30% da venda. 
# Faça um programa que informe o valor da comissão do vendedor para uma venda.


venda = int(input())

if venda < 1000:
  taxa = int(0)
elif venda >= 1000 and venda < 5000:
  taxa = float(0.1)
elif venda >= 5000 and venda < 10000:
  taxa = float(0.2)
elif venda >= 10000 and venda < 50000:
  taxa = float(0.25)
elif venda >= 50000:
  taxa = float(0.3)

total = venda*taxa

print(total)