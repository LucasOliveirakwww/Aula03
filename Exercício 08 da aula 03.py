##Algoritmo que leia e calcule o número de Litros e o tipo vendido para o cliente
Quantidade = float(input("Quantidade em litros comprados: "))
Combustivel = input ("Qual o tipo de combustível \n"
                     "G para gasolina\n"
                     "E para Etanol: \n ")
vEta = 4.90
vGas = 5.80
#Calculo
if Combustivel == "G":
    ValorG = Quantidade*vGas
    print (f"Você abasteceu {Quantidade} litros e gastou {ValorG:.2f}")

elif Combustivel == "E":
    ValorE = Quantidade * vEta
    print (f"Você abasteceu {Quantidade} litros e gastou {ValorE:.2f}")



