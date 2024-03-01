import os
import subprocess

def backup_and_protect_files(indexed_folder, backup_directory):
    # Verificar si el directorio de respaldo existe, si no, crearlo
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        subprocess.run(['sudo', 'chmod', 'u+w', backup_directory])  # Permitir escritura al usuario propietario

    # Iterar sobre cada archivo dentro de la carpeta indexada
    for root, dirs, files in os.walk(indexed_folder):
        # Crear la estructura de directorios en el directorio de respaldo
        relative_path = os.path.relpath(root, indexed_folder)
        backup_directory_path = os.path.join(backup_directory, relative_path)
        os.makedirs(backup_directory_path, exist_ok=True)

        # Copiar archivos y establecer permisos
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Construir la ruta de respaldo para el archivo
            backup_file_path = os.path.join(backup_directory_path, file_name)

            try:
                # Copiar el archivo al directorio de respaldo
                subprocess.run(['sudo', 'cp', file_path, backup_file_path])

                # Retirar los permisos de escritura y ejecución
                subprocess.run(['sudo', 'chmod', 'u-wx', backup_file_path])
                subprocess.run(['sudo', 'chmod', 'g-wx', backup_file_path])
                subprocess.run(['sudo', 'chmod', 'o-wx', backup_file_path])
            except Exception as e:
                print(f"No se pudo hacer copia de seguridad de {file_path}: {e}")

def backup_file(file_path, backup_directory):
    # Extract file name from file path
    file_name = os.path.basename(file_path)

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        subprocess.run(['sudo', 'chmod', 'u+w', backup_directory])  # Allow user write permission

    # Construct the backup file path
    backup_file_path = os.path.join(backup_directory, file_name)

    try:
        # Copy the file to the backup directory
        subprocess.run(['sudo', 'cp', file_path, backup_file_path])

        # Remove write and execute permissions
        subprocess.run(['sudo', 'chmod', 'u-wx', backup_file_path])
        subprocess.run(['sudo', 'chmod', 'g-wx', backup_file_path])
        subprocess.run(['sudo', 'chmod', 'o-wx', backup_file_path])
        
        print(f"Backup of {file_path} successful. Backup file location: {backup_file_path}")
    except Exception as e:
        print(f"Failed to backup {file_path}: {e}")

backup_and_protect_files('/home/kali/Desktop/pruebaspai1/', '/home/kali/Desktop/PAI 1 files/backup/')