import os
import csv
import hashlib
import logger, hash_generate, integrity_verifier


def file_indexer(directorio, archivo_csv):
    archivos_csv = []
    nombres = []
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as f:  # Abrir con UTF-8
        reader = csv.reader(f)
        next(reader)  # Saltar la fila de encabezado
        for row in reader:
            archivos_csv.append(row)
            nombres.append(row[0])

    with open(archivo_csv, 'a', newline='', encoding='utf-8') as f:  # Abrir con UTF-8

        for ruta, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(ruta, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, directorio)
                if ruta_relativa not in nombres:
                    writer = csv.writer(f)
                    sha1, sha256 = hash_generate.calcular_hashes(ruta_completa)
                    writer.writerow([ruta_relativa, sha1, sha256])
                else: 
                    index=nombres.index(ruta_relativa)
                    integrity_verifier.verificar_integridad(ruta_completa,archivos_csv[index])

            






