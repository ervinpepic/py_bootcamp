from pathlib import Path
from zipfile import ZipFile

with ZipFile("compressed.zip", "w") as zipF:
    for p in Path("modules/shopping").rglob("*.*"):
        # this will create zipped file in our current project direcotry
        zipF.write(p)

# To read from this zipped file we can create a read function

with ZipFile("compressed.zip") as zipFileRead:
    print(zipFileRead.namelist())
    info = zipFileRead.getinfo("modules/shopping/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zipFileRead.extractall("extrached_files")
