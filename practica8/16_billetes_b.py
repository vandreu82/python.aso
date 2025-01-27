#!/usr/bin/python
#
#   16.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
#   de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
#   Monedas: 2 €, 1 €. Ejemplo:
#       Introduzca una cantidad: 2343
#       4 billetes de 500
#       1 billete de 200
#       1 billete de 100
#       2 billetes de 20
#       1 moneda de 2
#       1 moneda de 1
#
#   Victor Manuel Andreu Felipe 2025

#!/usr/bin/python3

# Solicitar la cantidad de euros al usuario
cantidad = int(input("Introduzca una cantidad: "))

# Verificar que la cantidad sea positiva
if cantidad <= 0:
    print("La cantidad debe ser un número positivo.")
else:
    # Empezamos con la denominación más alta
    billete = 500

    while cantidad > 0:
        if cantidad >= billete:
            num_billetes = cantidad // billete  # Número de billetes o monedas de esta denominación
            cantidad %= billete  # Actualizamos la cantidad restante
            
            # Determinar si es billete o moneda
            if billete >= 5:
                tipo = "billete"
            else:
                tipo = "moneda"
            
            # Imprimir resultado sin usar {}
            if num_billetes > 1:
                print(str(num_billetes) + " " + tipo + "s de " + str(billete) + "€")
            else:
                print(str(num_billetes) + " " + tipo + " de " + str(billete) + "€")
        
        # Pasar a la siguiente denominación sin listas
        if billete == 500:
            billete = 200
        elif billete == 200:
            billete = 100
        elif billete == 100:
            billete = 50
        elif billete == 50:
            billete = 20
        elif billete == 20:
            billete = 10
        elif billete == 10:
            billete = 5
        elif billete == 5:
            billete = 2
        elif billete == 2:
            billete = 1
        else:
            break  # Terminamos cuando ya no hay más denominaciones
