print("~~~~~~~~~~~~~~~~~~~~")
valor = int (input("Sacar cédulas de 10 a 500: "))

print("~~~~~~~~~~~~~~~~~~~~")
cem = int(valor/100)
valor = valor % 100
print("Cédulas de R$ 100,00 =", cem)

cinquenta = int(valor/50)
valor = valor % 50
print("Cédulas de R$ 50,00 =", cinquenta)

dez = int(valor/10)
valor = valor % 10
print("Cédulas de R$ 10,00 =", dez)

cinco = int(valor/5)
valor = valor % 5
print("Cédulas de R$ 5 =", cinco)

dois = int(valor/2)
valor = valor % 2
print("Cédulas de R$ 2 =", dois)
print("~~~~~~~~~~~~~~~~~~~~")