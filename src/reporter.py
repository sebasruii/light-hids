import tkinter as tk
from datetime import datetime, timedelta
import os

def generate_report(directory_monthly_report, start_date, end_date):
    number_of_compromised_files = 0
    compromised_file_names = []
    try:
        # Check if integrity_log.txt exists
        log_file_path = 'integrity_log.txt'
        if not os.path.exists(log_file_path):
            print("integrity_log.txt does not exist.")
            # Create a report stating that no files have been compromised
            with open(os.path.join(directory_monthly_report, f'report_{start_date}_{end_date}.txt'), 'w') as f:
                f.write(f'Number of compromised files between {start_date} and {end_date}: 0\n')
                f.write('No files have been compromised in this period.\n')
            return

        with open(log_file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(" - ")
                log_date = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                if start_date <= log_date <= end_date:
                    number_of_compromised_files += 1
                    compromised_file_names.append(parts[1].split(':')[1].strip())

        with open(os.path.join(directory_monthly_report, f'report_{start_date}_{end_date}.txt'), 'w') as f:
            f.write(f'Number of compromised files between {start_date} and {end_date}: {number_of_compromised_files}\n')
            if number_of_compromised_files == 0:
                f.write('No files have been compromised in this period.\n')
            else:
                f.write('The files that have been compromised are:\n')
                for name in compromised_file_names:
                    f.write(name + '\n')
                
        print(f"Report generated successfully: report_{start_date}_{end_date}.txt")
    except Exception as e:
        print(f"Error: An exception occurred while generating the report: {e}")
