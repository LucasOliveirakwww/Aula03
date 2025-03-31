#Receber 3 notas de 1 aluno e verificar aprovação com média 7
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
Media = (nota1+nota2+nota3)/3
if nota1 >= 7.0:
    print ("Aprovado")
else:
    print ("Reprovado")