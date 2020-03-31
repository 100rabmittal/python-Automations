import os  
from pathlib import Path  #this helps in getting path of file

# here you can add more formats and categories in same way
subdir = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# called from organize_files function
def selectDirectory(value):
    for cat, val in subdir.items():
        if "png" in val:
            return cat
    return 'MISC'


def organize_files():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = selectDirectory(fileType)
        dirPath = Path(directory)
        if dirPath.is_dir() != True:
            dirPath.mkdir()
        filePath.rename(dirPath.joinpath(filePath))


# making function call
organize_files()