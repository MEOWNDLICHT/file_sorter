""" Asks the user for file directory. """

from pathlib import Path
import time


NEWLINE = "-----------------------------------------------------------------------------------------------"


def get_file_dir():
    """ Asks the users for file path/directory to start the sorting process. """
    print(f"\nThe current working directory is: '{Path.cwd()}'\n")
    
    while True:
        print(NEWLINE)
        file_dir = str(input("Enter the file directory here -> "))

        # detects empty values in when prompted to enter a file directory
        if file_dir.strip() is None or file_dir.strip() == '':
            print("Empty inputs detected.\n")
            continue

        # checks if the path do not exists
        elif not Path(file_dir).is_dir():
            print(f"Path '{file_dir}' do not exist.\n")
            continue

        print("Path found!")
        print("Sorting now...\n")
        time.sleep(3)
        return Path(file_dir)