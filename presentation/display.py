""" handles display and CLI-based interactions. """

from pathlib import Path
from services import get_file_dir, sort_files


def greet():
    """ Greets the user when the program starts. """
    print('\nWelcome, user!')
    print('This program aims to provide basic file sorting service according to file type.')


def how_to_use():
    """ Provides the basic commands and how-to that users will need to navigate the program. """
    print('\nHow to use:')
    print('Enter the full path of the directory which you want to sort out.')
    print('Automatically exits the program when sorting is successful.\n')


def main_display():
    greet()
    how_to_use()
    file_dir = get_file_dir()
    sort_files(file_dir)
