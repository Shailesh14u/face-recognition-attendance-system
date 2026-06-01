from tkinter import *


class Help:

    def __init__(self, root):

        self.root = root
        self.root.geometry("900x650+250+100")
        self.root.title("Help Center")
        self.root.configure(bg="white")

        # Title
        title_lbl = Label(
            self.root,
            text="HELP & USER GUIDE",
            font=("Times New Roman", 28, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=10
        )
        title_lbl.pack(fill=X)

        # Main Frame
        main_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )
        main_frame.place(x=20, y=80, width=850, height=500)

        sections = [
            ("📋 Student Management",
             "Add, Update, Delete and Manage Student Records"),

            ("📸 Photo Sample",
             "Capture Face Dataset for Training"),

            ("🧠 Train Data",
             "Train Face Images and Generate classifier.xml"),

            ("👁 Face Recognition",
             "Recognize Faces and Mark Attendance"),

            ("📊 Attendance",
             "View, Import and Export Attendance Records"),

            ("👨‍💻 Developer",
             "Developer Information and Project Details")
        ]

        y = 20

        for title, desc in sections:

            Label(
                main_frame,
                text=title,
                font=("Times New Roman", 16, "bold"),
                fg="darkblue",
                bg="white"
            ).place(x=20, y=y)

            Label(
                main_frame,
                text=desc,
                font=("Times New Roman", 12),
                bg="white"
            ).place(x=50, y=y+30)

            y += 75

        # Footer
        footer = Frame(
            self.root,
            bg="#1E3A8A"
        )

        footer.pack(side=BOTTOM, fill=X)

        Label(
            footer,
            text="📧 Support: shailesh.m0825@gmai.com     |      Version: 1.0",
            font=("Times New Roman", 12, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=8
        ).pack()