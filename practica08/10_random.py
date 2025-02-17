#!/usr/bin/python
#
#    10.- Escribir un programa que tome 100 números aleatorios entre 0 y 99. A continuación debe
#    mostrar cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y
#    [80-99]. Ejemplo:
#       [ 0-19]: 12
#       [20-39]: 34
#       [40-59]: 20
#       [60-79]: 15
#       [80-99]: 19
#       Total: 100
#
#   Victor Manuel Andreu Felipe 2025

import random

ran1 = 0
ran2 = 0
ran3 = 0
ran4 = 0
ran5 = 0

for i in range(1, 101, 1):
    num = random.randint(1, 99)
    if num >= 0 and num <= 19:
        ran1 += 1
    elif num >= 20 and num <39:
        ran2 += 1
    elif num >= 40 and num <59:
        ran3 += 1
    elif num >= 60 and num <79:
        ran4 += 1
    else:
        ran5 += 1

print("[ 0-19]: ", ran1)
print("[20-39]: ", ran2)
print("[40-59]: ", ran3)
print("[60-79]: ", ran4)
print("[80-99]: ", ran5)
print("Total: ", i)