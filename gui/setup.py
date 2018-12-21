from cx_Freeze import setup, Executable
import sys

base = 'WIN32GUI' if sys.platform == "win32" else None

# executables = [Executable("hello.py", base=base, icon='icon.ico')]
executables = [Executable("gui/__init__.py", base=base)]

packages = []
include_files = ['gui/ui.css']
options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files
    },

}

setup(
    name="test",
    options=options,
    version="1.0",
    description='desc of program',
    executables=executables
)
