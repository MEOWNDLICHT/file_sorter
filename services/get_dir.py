""" Asks the user for file directory. """

from pathlib import Path
import time


NEWLINE = "-----------------------------------------------------------------------------------------------"


def get_file_dir():
    """ Asks the users for file path/directory to start the sorting process. """
    print(NEWLINE)
    print(f"\nThe current working directory is: '{Path.cwd()}'\n")
    
    while True:
        file_dir = str(input("Enter the file directory here -> "))

        # detects empty values in when prompted to enter a file directory
        if file_dir.strip() is None or file_dir.strip() == '':
            print("\nEmpty inputs detected.\n")
            continue

        # checks if the path do not exists
        elif not Path(file_dir).is_dir():
            print(f"\nPath '{file_dir}' do not exist.\n")
            continue

        print("\nPath found!")
        print("Sorting now...\n")
        time.sleep(1)
        return Path(file_dir)