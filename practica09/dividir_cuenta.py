def dividir_cuenta():
    """Solicita nombres y cantidades aportadas, y divide la cuenta a partes iguales."""
    usuarios = []
    aportes = []
    
    print("Introduce los nombres de los usuarios y las cantidades que aportaron. Pulsa ENTER para finalizar.")
    while True:
        nombre = input("Nombre del usuario: ").strip()
        if nombre == "":
            break
        try:
            cantidad = float(input(f"Cantidad aportada por {nombre}: ").strip())
            usuarios.append(nombre)
            aportes.append(cantidad)
        except ValueError:
            print("Entrada no válida. Introduce un número válido.")
    
    if not usuarios:
        print("No se han introducido datos.")
        return
    
    total = sum(aportes)
    partes_iguales = total / len(usuarios)
    
    print("\nResumen de la cuenta:")
    print(f"Total aportado: {total:.2f}€")
    print(f"Cada persona debe pagar: {partes_iguales:.2f}€")
    
    diferencias = {usuarios[i]: aportes[i] - partes_iguales for i in range(len(usuarios))}
    
    deudores = {k: v for k, v in diferencias.items() if v < 0}
    acreedores = {k: v for k, v in diferencias.items() if v > 0}
    
    for usuario, diferencia in diferencias.items():
        if diferencia > 0:
            print(f"{usuario} ha pagado {diferencia:.2f}€ de más.")
        elif diferencia < 0:
            print(f"{usuario} debe {abs(diferencia):.2f}€ para equilibrar la cuenta.")
        else:
            print(f"{usuario} ha pagado exactamente su parte.")
    
    print("\nPara equilibrar la cuenta:")
    for deudor, deuda in deudores.items():
        for acreedor, credito in list(acreedores.items()):
            if abs(deuda) <= credito:
                print(f"{deudor} debe pagar {abs(deuda):.2f}€ a {acreedor}.")
                acreedores[acreedor] -= abs(deuda)
                break
            else:
                print(f"{deudor} debe pagar {credito:.2f}€ a {acreedor}.")
                deudores[deudor] += credito
                del acreedores[acreedor]
    
# Ejecutar la función
dividir_cuenta()
