from cx_Freeze import setup, Executable
import sys

base = "Win32GUI" if sys.platform == "win32" else None

build_exe_options = {
    "packages": [
        "tkinter",
        "cv2",
        "PIL",
        "mysql.connector"
    ],
    "include_files": [
        "Face data",
        "Attendance",
        "haarcascade_frontalface_default.xml",
        "classifier.xml",
        "developer",
        "database"
    ]
}

setup(
    name="Face Recognition Attendance System",
    version="1.0",
    description="Developed By Shailesh Maurya",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "login.py",
            base="gui"
        )
    ]
)