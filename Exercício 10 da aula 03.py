#Desafio dos horários, 12 e 24.
EntradaH1 = int(input("Hora de entrada -sem minutos-: "))
EntradaM1 = int(input("Minuto de entrada: "))
EntradaH2 = int(input("Hora de entrada -sem minutos-:"))
EntradaM2 = int(input("Minuto de entrada: "))
if EntradaH1 > 12:
                EntradaH1 = EntradaH1 - 12
if EntradaH2 > 12:
                EntradaH2 = EntradaH2 - 12
somaH = EntradaH1 + EntradaH2
if somaH > 12:
    somaH = somaH - 12
print(somaH)
if EntradaM1 > 60:
    EntradaM1 = EntradaM1 - 60
if EntradaM2 > 60:
    EntradaM2 = EntradaM2 - 60
somaM = EntradaM1 + EntradaM2
if somaM > 60:
    EntradaM1 + EntradaM2 - 60
print (somaM)







