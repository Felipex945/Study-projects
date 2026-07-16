import random
from time import sleep

computador = random.randint(0, 5)

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
print("-=-" * 20)

jogador = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print(f"PARABÉNS! Você conseguiu me vencer! O número era {computador}.")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")