import sys
from cx_Freeze import executable, setup, Executable

base = None
if sys.platform == 'win32' :
    base = 'Win32GUI'

setup(name = 'Program', version = '1.0', description = "BMI", executables = [Executable('BMI111.py', base = base)] )