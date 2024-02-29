import tkinter as tk
from tkinter import filedialog
import hash_generate
import os
import indexer
import backup
import sys
import time
import reporter
from datetime import datetime, timedelta

def verificar_existencia_archivo_superior(ruta_csv_superior):
    if os.path.exists(ruta_csv_superior):
        return True
    else:
        return False
    
def obtener_ruta_relativa_csv(archivo_csv):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_superior = os.path.abspath(os.path.join(directorio_actual, os.pardir))
    ruta_csv = os.path.join(directorio_superior, archivo_csv)
    return os.path.relpath(ruta_csv, directorio_actual)

def execute_main(directorio, directorio_backup, hashes_csv, periodicity_value, periodicity_unit, report_save_path, runs=1):
    backup.backup_and_protect_files(directorio, directorio_backup)
    if not verificar_existencia_archivo_superior(hashes_csv):
        hash_generate.generar_csv(directorio, hashes_csv)
    indexer.file_indexer(directorio, hashes_csv, directorio_backup)
    
    # Calculate the delay based on the selected periodicity
    if periodicity_unit == "Minutes":
        delay = periodicity_value * 60
    else:
        delay = periodicity_value * 60 * 60 * 24

    # Wait for the specified delay and then rerun the program
    time.sleep(delay)
    if runs % 30 == 0:
        reporter.generate_report(report_save_path, datetime.now()-timedelta(days=30), datetime.now())
    execute_main(directorio, directorio_backup, hashes_csv, periodicity_value, periodicity_unit, report_save_path, runs + 1)

def browse_directory(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def create_gui():
    root = tk.Tk()
    root.title("Application")

    tk.Label(root, text="Directorio:").grid(row=0, column=0, sticky="w")
    directorio_entry = tk.Entry(root)
    directorio_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_directory(directorio_entry)).grid(row=0, column=2)

    tk.Label(root, text="Directorio Backup:").grid(row=1, column=0, sticky="w")
    directorio_backup_entry = tk.Entry(root)
    directorio_backup_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_directory(directorio_backup_entry)).grid(row=1, column=2)

    tk.Label(root, text="Hashes CSV:").grid(row=2, column=0, sticky="w")
    hashes_csv_entry = tk.Entry(root)
    hashes_csv_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(hashes_csv_entry)).grid(row=2, column=2)

    tk.Label(root, text="Periodicity:").grid(row=3, column=0, sticky="w")
    periodicity_entry = tk.Entry(root)
    periodicity_entry.grid(row=3, column=1, padx=5, pady=5)
    periodicity_unit = tk.StringVar(root)
    periodicity_unit.set("Minutes")
    tk.OptionMenu(root, periodicity_unit, "Minutes", "Days").grid(row=3, column=2)

    tk.Label(root, text="Report Save Path:").grid(row=4, column=0, sticky="w")
    report_save_path_entry = tk.Entry(root)
    report_save_path_entry.grid(row=4, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_directory(report_save_path_entry)).grid(row=4, column=2)

    execute_button = tk.Button(root, text="Execute", command=lambda: execute_main(directorio_entry.get(), directorio_backup_entry.get(), hashes_csv_entry.get(), int(periodicity_entry.get()), periodicity_unit.get(), report_save_path_entry.get()))
    execute_button.grid(row=5, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run this script with sudo or as root.")
        sys.exit(1)
    create_gui()
