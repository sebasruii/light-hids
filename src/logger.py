from datetime import datetime

def log_compromised_file(file_name, location, log_file='integrity_log.txt'):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{current_time} - File integrity compromised at {location}: {file_name}"
    with open(log_file, 'a') as f:
        f.write(message + '\n')

# # Example usage:
# file_name = "example.txt"
# location = "/path/to/example"
# log_compromised_file(file_name, location)
