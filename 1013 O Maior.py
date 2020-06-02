# Faça um programa que leia três valores e apresente o maior dos três valores lidos
# seguido da mensagem “eh o maior”.
# Utilize a fórmula:
# # Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
# Um segundo passo, portanto é necessário para chegar no resultado esperado.

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

maiorAB = (A+B+abs(A-B))/2

maiorABC = (maiorAB+C+abs(maiorAB-C))/2
maior = int(maiorABC)
print('{} eh o maior'.format(maior))