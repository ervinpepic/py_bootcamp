# When we working with PATHS in Python, we can import PATH class to make job easier.
# First we need to import PATH from pathlib

from pathlib import Path

# Path(r"C:\Program Files\Windows\System32") # in Windows we can set path like this
# Path("/usr/local/bin") # in Linux Systems we can set path like this
# Path() # this is the path of the current working diretcotry
# Path() / "modules/shopping" / "__init__.py" # we can conactinate paths like this
# Path.home() # or we can get home dir with this builtin function in path class HOME

path = Path("modules/shopping/__init__.py") # set shopping direcotry as active dir

# we listed bellow some usefull methods for working with paths

print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path.absolute())