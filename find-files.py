#!/urs/bin/env pyhton3
import os

# Get the current directory
current_directory = os.getcwd()

# Initialize counters
file_count = 0
directory_count = 0

# Initialize lists
files = []
directories = []

# Loop through the directory contents
for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    if os.path.isfile(item_path):
        file_count += 1
        files.append(item)
    elif os.path.isdir(item_path):
        directory_count += 1
        directories.append(item)

# Print the counts and lists
print(f"Number of files: {file_count}")
print("Files:")
for file in files:
    print(f"  {file}")

print(f"Number of directories: {directory_count}")
print("Directories:")
for directory in directories:
    print(f"  {directory}")

