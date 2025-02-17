import sqlite3

# muestra toda la información almacenada en la base de datos
def show_server_info():
    conn = sqlite3.connect("server_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM server_info")
    rows = cursor.fetchall()
    
    if not rows:
        print("No hay datos almacenados en la base de datos.")
        return
    
    print("\nInformación almacenada en la base de datos:")
    for row in rows:
        print("----------------------------------")
        print(f"IP: {row[0]}")
        print(f"Hostname: {row[1]}")
        print(f"Machine ID: {row[2]}")
        print(f"Distro: {row[3]}")
        print(f"Procesador: {row[4]}")
        print(f"Tiempo encendido: {row[5]}")
        print(f"Carga: {row[6]}")
        print(f"Memoria Total: {row[7]}")
        print(f"Memoria Libre: {row[8]}")
        print(f"Versión de SSH: {row[9]}")
        print(f"Última actualización: {row[10]}")
    
    conn.close()

if __name__ == "__main__":
    show_server_info()