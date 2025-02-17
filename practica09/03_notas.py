#!/usr/bin/python
#
#   3.- Escribe un programa que vaya leyendo notas de alumnos, el programa dejará de pedir notas
#   cuando se pulse la tecla ENTER, al terminar el programa mostrará las notas de los alumnos y un
#   resumen de aprobados y suspensos incluyendo la nota media:
#       Introduzca las notas, ENTER para terminar:
#           Nota del alumno 1: 5.60
#           Nota del alumno 2: 4.20
#           Nota del alumno 3: (pulsamos ENTER)
#       Se han introducido las siguientes notas:
#           Alumno 01: 5.60
#           Alumno 02: 4.20
#       Resumen:
#           Número de alumnos: 2
#           Aprobados: 1
#           Suspensos: 1
#           Nota media: 4.9
#
#   Victor Manuel Andreu Felipe 2025

def leer_notas():
    notas = []
    contador = 1

    print("Introduzca las notas, ENTER para terminar:")
    while True:
        entrada = input(f"Nota del alumno {contador}: ")
        
        if entrada == "":  # Si el usuario pulsa ENTER sin escribir nada
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:  # Validación de nota válida
                notas.append(nota)
                contador += 1
            else:
                print("Por favor, introduce una nota entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Introduce un número o pulsa ENTER para terminar.")

    return notas

def mostrar_resumen(notas):
    print("\nSe han introducido las siguientes notas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Alumno {i:02d}: {nota:.2f}")

    aprobados = sum(1 for nota in notas if nota >= 5)
    suspensos = len(notas) - aprobados
    nota_media = sum(notas) / len(notas) if notas else 0

    print("\nResumen:")
    print(f"Número de alumnos: {len(notas)}")
    print(f"Aprobados: {aprobados}")
    print(f"Suspensos: {suspensos}")
    print(f"Nota media: {nota_media:.2f}")

# Programa principal
notas = leer_notas()
mostrar_resumen(notas)
