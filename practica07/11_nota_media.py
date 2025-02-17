#!/usr/bin/python
#
#    11.- Programa que lee la nota de 5 alumnos y dice cuántos están aprobados y cuál es la nota
#    media. Para este ejercicio no se pueden utilizar bucles.
#        Nota del alumno 01: 5.60
#        Nota del alumno 02: 4.20
#        Nota del alumno 03: 8.35
#        Nota del alumno 04: 7.23
#        Nota del alumno 05: 5.01
#        Aprobados: 4
#        Suspensos: 1
#        Nota media: 6.08
#
#   Victor Manuel Andreu Felipe 2025
#   

apro = 0    # iniciamos los contadores
susp = 0

nota1 = float(input("Nota del alumno 01: "))
nota2 = float(input("Nota del alumno 02: "))
nota3 = float(input("Nota del alumno 03: "))
nota4 = float(input("Nota del alumno 04: "))
nota5 = float(input("Nota del alumno 05: "))

# control de rangos

if (nota1 < 0 or nota1 > 10 or
    nota2 < 0 or nota2 > 10 or
    nota3 < 0 or nota3 > 10 or
    nota4 < 0 or nota4 > 10 or
    nota5 < 0 or nota5 > 10):
    print("Deben ser notas entre 0 y 10")
else:
    # incrementamos aprobados o suspensos
    if nota1 < 5:
        susp += 1
    else:
        apro += 1

    if nota2 < 5:
        susp += 1
    else:
        apro += 1

    if nota3 < 5:
        susp += 1
    else:
        apro += 1

    if nota4 < 5:
        susp += 1
    else:
        apro += 1

    if nota5 < 5:
        susp += 1
    else:
        apro += 1

    print("Aprobados: ", apro)
    print("Suspensos: ", susp)
    print("Nota media: ", (nota1 + nota2 + nota3 + nota4 + nota5) / 5)
