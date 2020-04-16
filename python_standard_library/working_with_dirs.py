from pathlib import Path

path = Path("python_standard_library")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("some_name")

for paths in path.iterdir():
    print(paths)

# if we have a direcotry with thousands of files
# we need to convert it to the arrays using list comprehension

p = [paths for paths in path.iterdir() if paths.is_dir()]
print(p)


# if we want to search recursively we must use rglob
py_files = [files for files in path.rglob("*.py")]
print(py_files)
