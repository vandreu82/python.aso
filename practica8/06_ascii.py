#!/usr/bin/python
#
#   6.- Escribir un programa que muestre la tabla ASCII. Extracto:
#       Tabla ASCII (caracteres de 32 a 126):
#       …
#       60 => <
#       61 => =
#       62 => >
#       63 => ?
#       64 => @
#       65 => A
#       66 => B
#       ...
#
#   Victor Manuel Andreu Felipe 2025

print("Tabla ASCII (caracteres de 32 a 126):")

for i in range(32, 127):
    print(i,"=>",chr(i))