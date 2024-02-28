import logger, hash_generate


def verificar_integridad(ruta, datos):
    sha1_csv = datos[1]
    sha256_csv  = datos[2]
    sha1, sha256 = hash_generate.calcular_hashes(ruta)
    if sha1 != sha1_csv or sha256 != sha256_csv:
        print(f"El archivo {ruta} ha sido modificado.")
        file_name=ruta.split("\\")
        logger.log_compromised_file(file_name,ruta)


            



