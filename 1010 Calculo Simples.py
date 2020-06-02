# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
# o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
# Após, calcule e mostre o valor a ser pago.,

cod,nubPec,vUnit = input().split()
cod = int(cod)
nubPec = int(nubPec)
vUnit = float(vUnit)

cod2,nubPec2,vUnit2 = input().split()
cod2 = int(cod2)
nubPec2 = int(nubPec2)
vUnit2 = float(vUnit2)

# cod = int(input())
# nubPec = int(input())
# vUnit = float(input())
# cod2 = int(input())
# nubPec2 = int(input())
# vUnit2 = float(input())
total = nubPec*vUnit + nubPec2*vUnit2
print("VALOR A PAGAR: R$ {:.2f}".format(total))
