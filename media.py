n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print("A média é:",round(media))
if media >= 7:
    print("Aprovado")   
else:   
    print("Reprovado")
