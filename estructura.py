import os

def print_directory_structure(path, level=0):
    # Iterar sobre cada directorio y archivo en la ruta
    for root, dirs, files in os.walk(path):
        # Imprimir el directorio actual
        print("  " * level + f"📁 {os.path.basename(root)}/")
        
        # Incrementar el nivel para los subdirectorios
        for d in dirs:
            print("  " * (level + 1) + f"📂 {d}/")
        
        # Imprimir los archivos
        for f in files:
            print("  " * (level + 1) + f"📄 {f}")
        
        # Romper después de la raíz si no deseas recorrer en profundidad
        break

# Ruta que deseas explorar
path = r"C:\Users\jadarve\OneDrive - Grupo Bancolombia\Bancolombia\MIAD\Despliegue de soluciones de analytics\Proyecto\fraud-detection"  # Usa '.' para la carpeta actual o especifica otra ruta
print_directory_structure(path,1)
