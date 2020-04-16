from pathlib import Path
from time import ctime
from shutil import copy

source = Path("python_standard_library/__init__.py")
target = Path() / "modules"
copy(source, target)

# other methdos
path = Path("python_standard_library/__init__.py")
# Path.exist()
# Path.rename()
# Path.unlink()
print(ctime(path.stat().st_ctime()))
