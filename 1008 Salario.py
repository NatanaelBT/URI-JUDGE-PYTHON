# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
# o valor que recebe por hora e calcula o salário desse funcionário.
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

number = int(input())
hours = int(input())
valueHours = float(input())

salary = hours * valueHours

print("NUMBER = {}".format(number))
print("SALARY = U$ {:.2f}".format(salary))