""" Handles the sorting pattern and whatnot. """

from pathlib import Path
import shutil

NEWLINE = "-----------------------------------------------------------------------------------------------"

# sorting pattern (dict format)
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".csv", ".md", ".epub", ".tex"],
    
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".heic", ".raw"],
    
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"],
    
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".amr"],
    
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab", ".dmg", ".tgz", ".z"],
}



def categorize_file(file: str):
    """ Scans file and returns its category based on its extension
        Returns:
            str: File's category based on its extension. """
    file_ext = file.suffix
    for category, extension in FILE_TYPES.items():
        if file_ext in extension:
            return category
    return 'Miscellaneous'


def sort_file(file_dir:Path):
    """ Sorting logic """
    # scans the directory and categorizes each file
    for file in file_dir.iterdir():
        if file.is_file():
            file_category = categorize_file(file)

            # creates new folder for sorting if not yet made
            sorting_folder = file_dir / file_category
            if not sorting_folder.exists():
                sorting_folder.mkdir(parents=True, exist_ok=True)
            
            # moves the file to its respective folder
            shutil.move(str(file), str(sorting_folder / file.name))
    print('Sorting Done!')
    print('Exiting the program...\n')
    print(NEWLINE)


def main_sorter(file_dir: Path):
    """ Handles the sorting flow. """
    sort_file(file_dir)