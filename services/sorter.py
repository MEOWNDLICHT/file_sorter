""" handles the sorting pattern and whatnot. """

from pathlib import Path


# sorting pattern (dict format)
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", 
                ".rtf", ".odt", ".csv", ".md", ".epub", ".tex"],
    
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", 
                ".svg", ".ico", ".heic", ".raw"],
    
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", 
            ".mpeg", ".mpg", ".3gp", ".m4v"],
    
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", 
            ".m4a", ".alac", ".aiff", ".amr"],
    
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", 
                ".xz", ".iso", ".cab", ".dmg", ".tgz", ".z"],
    
    "Miscellaneous": [] 
}


# shorthands for each file types
documents_ext = FILE_TYPES['Documents']
pictures_ext = FILE_TYPES['Pictures']
videos_ext = FILE_TYPES['Videos']
music_ext = FILE_TYPES["Music"]
archives_ext = FILE_TYPES['Archives']
misc_ext = FILE_TYPES['Miscellaneous']



def sort_files(file_dir: str):
    """ sorts files based on file types. """
    # scans directory for various file extension
    for file in file_dir:
        pass



    # creates folders for each file categories: documents, pics, music, vids, archives, and misc...
    for file_category in FILE_TYPES.keys():
        sorted_folder = Path(file_category)
        sorted_folder.mkdir()


    # moves similar files types to their respective categories