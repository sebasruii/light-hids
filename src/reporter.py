import tkinter as tk
from datetime import datetime

def generate_report(log_file, start_date, end_date):
    compromised_files = 0
    with open(log_file, 'r') as f:
        for line in f:
            parts = line.strip().split(" - ")
            log_date = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
            if start_date <= log_date <= end_date:
                compromised_files += 1
    return compromised_files

def show_report(log_file, start_date, end_date):
    num_compromised_files = generate_report(log_file, start_date, end_date)
    report_label.config(text=f"Number of compromised files between {start_date} and {end_date}: {num_compromised_files}")

def create_gui(start_date, end_date, log_file):
    window = tk.Tk()
    window.title("Incident Reporter")

    tk.Label(window, text="Log File Path:").pack()
    log_file_entry = tk.Entry(window)
    log_file_entry.insert(0, log_file)
    log_file_entry.config(state='readonly')
    log_file_entry.pack()

    tk.Label(window, text="Start Date (YYYY-MM-DD):").pack()
    start_date_entry = tk.Entry(window)
    start_date_entry.insert(0, start_date)
    start_date_entry.config(state='readonly')
    start_date_entry.pack()

    tk.Label(window, text="End Date (YYYY-MM-DD):").pack()
    end_date_entry = tk.Entry(window)
    end_date_entry.insert(0, end_date)
    end_date_entry.config(state='readonly')
    end_date_entry.pack()

    report_button = tk.Button(window, text="Generate Report", command=lambda: show_report(log_file, start_date, end_date))
    report_button.pack()

    global report_label
    report_label = tk.Label(window, text="")
    report_label.pack()

    window.mainloop()

# Example usage:
start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-02-29", "%Y-%m-%d")
log_file = "integrity_log.txt"
create_gui(start_date, end_date, log_file)
