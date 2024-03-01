import logger, hash_generate, restore


def verificar_integridad(ruta, datos, backup_directory, indexed_folder):
    sha1_csv = datos[1]
    sha256_csv  = datos[2]
    sha1, sha256 = hash_generate.calcular_hashes(ruta)
    if sha1 != sha1_csv or sha256 != sha256_csv:
        relative_path=ruta.split(indexed_folder)[1]
        print(f"El archivo {ruta} ha sido modificado.")
        file_name=ruta.split("/")[-1]
        logger.log_compromised_file(file_name,ruta)
        restore.restore_file_from_backup(relative_path, backup_directory, indexed_folder)


            



