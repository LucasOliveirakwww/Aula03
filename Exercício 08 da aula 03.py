##Algoritmo que leia e calcule o número de Litros e o tipo vendido para o cliente
Quantidade = float(input("Quantidade em litros comprados: "))
Combustivel = input ("Qual o tipo de combustível \n"
                     "G or g para gasolina\n"
                     "E or e para Etanol: \n ")
vEta = 4.90
vGas = 5.80
#Calculo
if Combustivel == 'G' or Combustivel =='g':
    ValorG = Quantidade*vGas
    print (f"Você abasteceu {Quantidade} litros e gastou {ValorG:.2f}")

elif Combustivel == 'E' or Combustivel == 'e':
    ValorE = Quantidade*vEta
    print (f"Você abasteceu {Quantidade} litros e gastou {ValorE:.2f}")



