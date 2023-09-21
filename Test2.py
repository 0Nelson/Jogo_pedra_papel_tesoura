# Jogo da pedra, papel ou tesoura
#
# Coder: Nelson Reis    V:0.0

# 01 - Instanciar as variáveis


import random

Jogador = input("Escolhe uma opção")
pc = random.choice(("pedra", "papel", "tesoura"))

# 02 - Lógica
if Jogador == "papel" and pc == "papel":
    resultado = "Jogador empatou"

if Jogador == "tesoura" and pc == "papel":
    resultado = "Jogador ganhou"

if Jogador == "pedra" and pc == "papel":
    resultado = "Jogador perdeu"

if Jogador == "papel" and pc == "tesoura":
    resultado = "Jogador ganhou"

if Jogador == "tesoura" and pc == "tesoura":
    resultado = "Jogador empatou"

if Jogador == "pedra" and pc == "tesoura":
    resultado = "Jogador ganhou"       

if Jogador == "papel" and pc == "pedra":
    resultado = "Jogador ganhou"

if Jogador == "tesoura" and pc == "pedra":
    resultado = "Jogador perdeu"

if Jogador == "pedra" and pc == "pedra":
    resultado = "Jogador empatou"       

# 03 - Resultado
print(resultado)
print("jogador ", Jogador, "PC: ", pc)
