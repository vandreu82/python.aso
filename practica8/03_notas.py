#!/usr/bin/python
#
#   3.- Programa que lee notas de los alumnos y dice cuántos están aprobados y cuál es la nota
#   media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.
#       Introduzca las notas, ENTER para terminar:
#       Nota del alumno 1: 5.60
#       Nota del alumno 2: 4.20
#       Nota del alumno 3: 8.35
#       Nota del alumno 4: 7.23
#       Nota del alumno 5: 5.01
#       Nota del alumno 6: (pulsamos ENTER)
#       Número de alumnos: 5
#       Aprobados: 4
#       Suspensos: 1
#       Nota media: 6.08
#
#   Victor Manuel Andreu Felipe 2025

print("Introduzca las notas, ENTER para terminar: ")

alu = 0
apro = 0
susp = 0
notasum = 0

while True:
    notastr = input("Nota del alumno " + str(alu + 1) + ": ")
    
    # el bucle se ejecutará siempre excepto cuando le metamos una cadena vacía
    if notastr == "":       
        break
    
    # convertimos la nota a float y comprobamos que sea correcta, si no, volvemos 
    # a iterar sin hacer nada
    nota = float(notastr)
    if nota < 0 or nota > 10:
        print("La nota debe estar comprendida entre 0 y 10")
        continue

    # acumulamos el número de alumnos y la suma de las notas
    # para calcular la media mas tarde
    alu += 1
    notasum += nota

    # incrementamos aprobados y suspensos
    if nota >= 5:
        apro += 1
    else:
        susp += 1

# comprobamos que haya notas

if alu > 0:
    print("Número de alumnos: ", alu)
    print("Aprobados: ", apro)
    print("Suspensos: ", susp)
    print("Nota media: ", notasum / alu)
else:
    print("No has introducido notas")
