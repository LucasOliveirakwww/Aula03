#Ler nome de 2 times, número de gols por time e escrever nome do vencedor ou empate
Team1 = input("Nome do primeiro time: ")
Team2 = input("Nome do segundo time: ")
TeamGols1 = input(f"Gols do(a) {Team1} na partida:")
TeamGols2 = input(f"Gols do(a) {Team2} na partida: ")
if TeamGols1 > TeamGols2:
    print(f"{Team1} ganhou {TeamGols1}")
else:
    if TeamGols2 > TeamGols1:
        print(f"{Team2} ganhou com {TeamGols2} gols")
    else:
        print(f"Empate de {TeamGols1},{TeamGols2}")