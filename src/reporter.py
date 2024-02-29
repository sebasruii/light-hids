import tkinter as tk
from datetime import datetime, timedelta

class ReportManager:

    def __init__(self, log_file):
        self.log_file = log_file
        self.counter = 0

    def _get_start_date(self):
        return datetime.now() - timedelta(days=self.counter)

    def _get_end_date(self):
        return datetime.now() - timedelta(days=self.counter - 29)

    def generate_report(self):
        compromised_files = 0
        with open(self.log_file, 'r') as f:
            for line in f:
                parts = line.strip().split(" - ")
                log_date = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                if self._get_start_date() <= log_date <= self._get_end_date():
                    compromised_files += 1
        return compromised_files

    def show_report(self):
        num_compromised_files = self.generate_report()
        report_label.config(text=f"Number of compromised files between {self._get_start_date()} and {self._get_end_date()}: {num_compromised_files}")
        self.counter += 1
        print(self.counter)
        if self.counter % 30 == 0:
            self.counter = 0

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
# start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
# end_date = datetime.strptime("2024-02-29", "%Y-%m-%d")
# log_file = "integrity_log.txt"
# create_gui(start_date, end_date, log_file)
