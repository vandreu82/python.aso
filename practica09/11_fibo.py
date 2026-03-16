#!/usr/bin/python
#
#   11.- En Matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números
#   naturales:
#       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#   Podemos definirla más formalmente así:
#       f0 = 0
#       f1 = 1
#       fn = fn – 1 + fn – 2 para n = 2, 3, 4, 5 ...

#   Escribe un programa que calcule los 100 primeros términos de la sucesión y los almacene
#   en una lista, para calcular el siguiente término el programa debe basarse en los dos anteriores
#   previamente calculados. Una vez calculados, el programa debe mostrarlos en pantalla.
#
#   Victor Manuel Andreu Felipe 2025

def fibonacci(n):
    fib_seq = [0, 1]  # inicializamos la lista con los dos primeros valores
    
    # iteramos para calcular el siguiente valor sumando los dos últimos
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq

# Generamos y mostramos los 100 primeros números de Fibonacci
fibonacci_100 = fibonacci(100)

print("Sucesión de Fibonacci (100 términos):")
for i, num in enumerate(fibonacci_100):
    print(f"F({i}) = {num}")

