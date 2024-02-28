import hash_generate
import os
import indexer


def verificar_existencia_archivo_superior():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_superior = os.path.abspath(os.path.join(directorio_actual, os.pardir))
    ruta_csv_superior = os.path.join(directorio_superior, "hashes.csv")

    if os.path.exists(ruta_csv_superior):
        return True
    else:
        return False
    
def obtener_ruta_relativa_csv(archivo_csv):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_superior = os.path.abspath(os.path.join(directorio_actual, os.pardir))
    ruta_csv = os.path.join(directorio_superior, archivo_csv)
    return os.path.relpath(ruta_csv, directorio_actual)


def main():
    directorio = "C:/Users/joaqu/Desktop/Rol"
    if not verificar_existencia_archivo_superior():
        hash_generate.generar_csv(directorio,"hashes.csv")

    hashes_csv = obtener_ruta_relativa_csv("hashes.csv")
    indexer.file_indexer(directorio,hashes_csv)


if __name__ == "__main__":
    main()


