#!/usr/bin/env python3
import os

def count_and_list_files_dirs():
    
    items = os.listdir('.')
    

    files = [item for item in items if os.path.isfile(item)]
    directories = [item for item in items if os.path.isdir(item)]
    num_files = len(files)
    num_directories = len(directories)
    print(f"Number of files: {num_files}")
    print(f"Number of directories: {num_directories}")
    print("\nFiles:")
    for file in files:
        print(file)
    
    print("\nDirectories:")
    for directory in directories:
        print(directory)
if __name__ == "__main__":
    count_and_list_files_dirs()

