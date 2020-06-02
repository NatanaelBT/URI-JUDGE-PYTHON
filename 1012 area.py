# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
# Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

pi = 3.14159

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

artri = (A * C)/2
arcir = pi * (C ** 2)
artrap = ((A+B)/2) * C
arquad = B**2
arretan = B * A

print('TRIANGULO: {:.3f}'.format(artri))
print('CIRCULO: {:.3f}'.format(arcir))
print('TRAPEZIO: {:.3f}'.format(artrap))
print('QUADRADO: {:.3f}'.format(arquad))
print('RETANGULO: {:.3f}'.format(arretan))
