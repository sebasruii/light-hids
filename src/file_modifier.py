import os
import random
import string

def modify_files(directory, num_files_to_modify, bytes_to_add):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        # Choose random files to modify
        files_to_modify = random.sample(files, min(num_files_to_modify, len(files)))
        
        for file_name in files_to_modify:
            file_path = os.path.join(directory, file_name)
            # Read the existing content
            with open(file_path, 'rb') as file:
                content = file.read()
            # Append bytes to the content
            modified_content = content + bytes_to_add
            # Write modified content back to the file
            with open(file_path, 'wb') as file:
                file.write(modified_content)
        
        print(f"{num_files_to_modify} files modified successfully.")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    num_files_to_modify = int(input("Enter the number of files to modify: "))
    bytes_to_add = bytes(input("Enter the bytes to add: "), 'utf-8')  # Convert string input to bytes
    modify_files(directory, num_files_to_modify, bytes_to_add)
