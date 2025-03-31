#Programa para ler nome, idade e salário para mostrar subsequentemente
nome = input ("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
salario = float(input("O seu salario é: "))
#Espaço amostral
print(f"Nome do indivíduo é {nome}, idade {idade}, salário {salario}")
#Calcular percentual de aumento
aumento = float(input("Valor do percentual aumentado: "))
calculo = salario * aumento / 100
#Resultado do aumento aditado
total = print(salario + calculo)