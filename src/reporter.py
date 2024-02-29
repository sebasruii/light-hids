import tkinter as tk
from datetime import datetime, timedelta

def generate_report(directory_monthly_report, start_date, end_date):
    number_of_compromised_files = 0
    compromised_file_names = []
    try:
        with open('integrity_log.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(" - ")
                log_date = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                if start_date <= log_date <= end_date:
                    number_of_compromised_files += 1
                    compromised_file_names.append(parts[1].split(':')[1].strip())

        with open(directory_monthly_report+'/report'+ str(start_date) + '-' + str(end_date) + '.txt', 'w') as f:
            f.write('Number of compromised files between ' + str(start_date) + ' ' + end_date + ': '+ number_of_compromised_files + '\n')
            f.write('The files that have been compromised are:\n')

            for name in compromised_file_names:
                f.write(name + '\n')
    except Exception as e:
        print(f"Error, an exception has occurred while generating the report: {e}")
        
