# Ejercicio 2: hash de ficheros
#   Crea un script que dado un directorio que se reciba por línea de parámetros, muestre un
#   listado de forma recursiva con la ruta completa de cada uno de los ficheros y su hash
#   SHA256. No se permite ejecutar ningún comando externo, la salida será similar a esta:
#
#   Víctor Manuel Andreu Felipe 2025



import os
import hashlib
import sys

# calcula el hash SHA256 de un archivo
def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except PermissionError:
        return "PERMISSION_DENIED"


# recorre los archivos de un directorio de forma recursiva
def list_files_with_hashes(directory):
    print(f"Procesando directorio {directory}:")
    print("=" * 30)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # comprobación de que existe
            if not os.path.exists(file_path):
                print(f"SKIPPED (File Not Found): {file_path}")
                continue
            
            # calculo del sha256
            file_hash = calculate_sha256(file_path)
            print(f"{file_hash} {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ejercicio2.py <directorio>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: El directorio especificado no existe o no es válido.")
        sys.exit(1)
    
    list_files_with_hashes(directory)
