""" asks the user for file directory. """

from pathlib import Path

NEWLINE = "-----------------------------------------------------------------------------------------------"

def get_file_dir():
    """ Asks the users for file path/directory to start the sorting process. 
    
        Returns:
            str: the file directory to be sorted."""
    print(NEWLINE)
    print(f"The current working directory is: '{Path.cwd()}'\n")

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

        print("Path found!")
        return Path(file_dir)