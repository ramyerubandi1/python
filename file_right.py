#!/usr/bin/env python3
import os
import stat

def display_file_rights(filename):
    try:

        file_stat = os.stat(filename)
        
        
        file_mode = file_stat.st_mode
        
        
        print(f"Permissions for '{filename}':")
        print(f"Read by owner: {'Yes' if file_mode & stat.S_IRUSR else 'No'}")
        print(f"Write by owner: {'Yes' if file_mode & stat.S_IWUSR else 'No'}")
        print(f"Execute by owner: {'Yes' if file_mode & stat.S_IXUSR else 'No'}")
        print(f"Read by group: {'Yes' if file_mode & stat.S_IRGRP else 'No'}")
        print(f"Write by group: {'Yes' if file_mode & stat.S_IWGRP else 'No'}")
        print(f"Execute by group: {'Yes' if file_mode & stat.S_IXGRP else 'No'}")
        print(f"Read by others: {'Yes' if file_mode & stat.S_IROTH else 'No'}")
        print(f"Write by others: {'Yes' if file_mode & stat.S_IWOTH else 'No'}")
        print(f"Execute by others: {'Yes' if file_mode & stat.S_IXOTH else 'No'}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")



filename = input("Enter the file name: ")
display_file_rights(filename)

