import os
import random
import string

def generate_random_name(length=8):
    """Generate a random name."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_files(folder_path, num_files=100):
    """Generate files with random names and extensions in the specified folder."""
    extensions = ['.txt', '.pdf', '.jpg', '.png', '.docx', '.xlsx', '.csv', '.mp3', '.mp4']
    try:
        os.makedirs(folder_path, exist_ok=True)
        for i in range(num_files):
            file_name = generate_random_name() + random.choice(extensions)
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w'):
                pass
        print(f"{num_files} files generated successfully in {folder_path}")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the directory path: ")
    num_files = 100
    generate_files(folder_path, num_files)
