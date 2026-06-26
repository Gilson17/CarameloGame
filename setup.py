import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["pygame", "sqlite3"],
    "include_files": ["asset/"]
}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CaramelGame",
    version="1.0",
    description="Game did in Pygame",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)