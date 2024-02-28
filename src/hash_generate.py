import os
import csv
import hashlib


def calcular_hashes(archivo):
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(archivo, 'rb') as f:
        while True:
            data = f.read(65536)  # Leer en bloques de 64KB
            if not data:
                break
            sha1.update(data)
            sha256.update(data)
    return sha1.hexdigest(), sha256.hexdigest()

def generar_csv(directorio, archivo_csv):
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as f:  # Especificar el encoding como utf-8
        writer = csv.writer(f)
        writer.writerow(['Archivo', 'SHA-1', 'SHA-256'])
        for ruta, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(ruta, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, directorio)
                sha1, sha256 = calcular_hashes(ruta_completa)
                writer.writerow([ruta_relativa, sha1, sha256])



