#17) Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a fórmula de Bhaskara.

a = float(input())
b = float(input())
c = float(input())
delta = (b**2)-(4*a*c)

x=(-b+((delta)**0.5))/(2*a)
print(x)