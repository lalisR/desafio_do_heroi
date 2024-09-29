# Logando no jogo
print("Olá, bem-vindo ao primeiro desafio do heroi.")
nome = str(input("Digite seu nome:"))
print("%s esta pronto para o desafio?" %(nome))

nivel = ["Ferro", "Broze", "Prata", "Platina", "Diamante", "Ascendente", "Imortal", "Radiante"]

#mostrando pontuaçao
pontuacao = int(input(f"Por favor {nome}, digite sua pontuação acumulada ate agora:"))
#comparaçao de pontos
if pontuacao < 1000:
    print(f"Seu nivel é: {nivel[0]}.")
elif pontuacao >=1001 and pontuacao < 2000:
    print(f"Seu nivel é: {nivel[1]}.")
elif pontuacao >=2001 and pontuacao < 3000:
    print(f"Seu nivel é: {nivel[2]}.")
elif pontuacao >= 3001 and pontuacao < 4000:
    print(f"Seu nivel é: {nivel[3]}.")
elif pontuacao >= 4001 and pontuacao < 5000:
    print(f"Seu nivel é: {nivel[4]}.")
elif pontuacao >= 5001 and pontuacao < 6000:
    print(f"Seu nivel é:{nivel[5]}.")
elif pontuacao >= 6001 and pontuacao < 8000:
    print(f"Seu nivel é: {nivel[6]}.")
elif pontuacao >= 8001 and pontuacao < 9000:
    print(f"Seu nivel é: {nivel[7]}.")
else:
    print(f"{nome} Reinicie o jogo, por favor")