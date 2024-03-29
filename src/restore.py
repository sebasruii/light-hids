import os
import subprocess
import shutil

def restore_file_from_backup(relative_path, backup_directory, indexed_folder):
    # Construir la ruta completa del archivo en el directorio de respaldo
    backup_file_path = os.path.join(backup_directory, relative_path[1:])

    # Construir la ruta de destino del archivo en la carpeta original
    destination_file_path = os.path.join(indexed_folder, relative_path[1:])
    print(indexed_folder)
    print(relative_path)
    print(backup_directory)
    print(destination_file_path)
    print(backup_file_path)

    try:
        subprocess.run(['sudo', 'rm', destination_file_path])
        # Copiar el archivo de respaldo a la ubicación original
        subprocess.run(['sudo', 'cp', backup_file_path, destination_file_path])
        print(f"Archivo restaurado exitosamente: {destination_file_path}")
    except Exception as e:
        print(f"No se pudo restaurar el archivo {destination_file_path}: {e}")

