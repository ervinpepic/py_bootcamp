import subprocess

try:
    completed = subprocess.run(["python3", 
    "/Users/ervinpepic/Documents/Development/DesktopApps/PythonApps/py_bootcamp/python_standard_library/incluede_this.py"], 
    capture_output=True, text=True, check=True)

    print("args", completed.args)
    print("returned code", completed.returncode)
    print("Error", completed.stderr)
    print("output", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
