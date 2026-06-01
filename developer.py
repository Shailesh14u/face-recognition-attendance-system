from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import csv
import os

class Developer:

    def __init__(self, root):

        self.root = root
        self.root.geometry("800x600+200+100")
        self.root.title("Developer Information")
        self.root.configure(bg="#F1F5F9")

        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )

        title_lbl.pack(fill=X)

        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=50, y=80, width=700, height=450)

        # DETAILS SECTION

        Label(
            main_frame,
            text="Shailesh Maurya",
            font=("Times New Roman", 24, "bold"),
            fg="darkblue"
        ).place(x=200, y=20)

        Label(
            main_frame,
            text="BE CSE (Artificial Intelligence & Machine Learning)",
            font=("Times New Roman", 14, "bold")
        ).place(x=200, y=60)

        Label(
            main_frame,
            text="Email: shailesh.m0825@gmail.com",
            font=("Times New Roman", 14)
        ).place(x=200, y=95)

        Label(
            main_frame,
            text="Project: Face Recognition Attendance System",
            font=("Times New Roman", 14, "bold"),
            fg="green"
        ).place(x=200, y=130)


        summary = """
            ABOUT ME

            I am Shailesh Maurya, currently pursuing BE in Computer Science Engineering with
            specialization in Artificial Intelligence and Machine Learning.
            I am passionate about AI, Computer Vision, Automation and Software Development.
            PROJECT DETAILS
            This Face Recognition Attendance System uses Python, OpenCV, Tkinter and MySQL
            to automate attendance through real-time face detection and recognition.

            This project reduces manual attendance
            effort and improves accuracy through
            AI-powered face recognition.
            """
        Label(
            main_frame,
            text=summary,
            justify=LEFT,
            font=("Times New Roman", 13),
        ).place(x=-10, y=170,width=650)




        img = Image.open("D:\Face Recognition\developer\developer.jpeg")
        img = img.resize((150,150))
        self.photoimg = ImageTk.PhotoImage(img)

        photo_lbl = Label(main_frame, image=self.photoimg)
        photo_lbl.place(x=20, y=10, width=150, height=150)


        # ========Footer======
        footer = Frame(
            self.root,
            bg="#1E3A8A"
        )

        footer.place(
            x=00,
            y=560,
            width=800,
            height=50
            )

        Label(
            footer,
            text="📧 Support: shailesh.m0825@gmail.com | Version: 1.0",
            font=("Segoe UI", 10, "bold"),
            bg="#1E3A8A",
            fg="white"
            ).pack(pady=8)



if __name__ == "__main__":

    root = Tk()

    obj = Developer(root)

    root.mainloop()