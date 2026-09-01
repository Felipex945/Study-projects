'''from math import factorial
numero = int(input("Digite um valor para calcular seu fatorial: "))
fatorial = factorial(numero)
print(f"O fatorial do número {numero} é {fatorial}")'''

n = int(input("Digite um número para o cálculo do seu fatorial: "))
c = n
while c > 0:
    print(f"{c}", end=' -> ')
    c -= 1