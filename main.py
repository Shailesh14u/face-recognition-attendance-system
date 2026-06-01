from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from developer import Developer
from train import Train
from face_recognation import Face_Recognition
from attendance import Attendance
from help import Help
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.configure(bg="#F1F5F9")

        #TITLE
        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )
        title_lbl.place(x=-200, y=0, width=1920, height=50)


        dashboard_frame = Frame(
            self.root,
            bg="#F1F5F9"
        )

        dashboard_frame.place(
             x=100,
            y=100,
            width=1450,
            height=700
        )

        # BACKGROUND IMAGE
        # img = Image.open("images/bg.jpg")
        # img = img.resize((1920, 1080), Image.LANCZOS)

        # self.photoimg = ImageTk.PhotoImage(img)

        # bg_img = Label(self.root, image=self.photoimg)
        # bg_img.place(x=0, y=55, width=1920, height=1025)

        #STUDENT BUTTON
        student_btn = Button(
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        student_btn.place(x=200, y=100, width=250, height=60)


    # Detect Face
        detect_btn = Button(
        text="Detect Face",
        command=self.face_recognation,
        cursor="hand2",
       bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
         )

        detect_btn.place(x=550, y=100, width=250, height=60)


    #ATTENDANCE BUTTON
        attendance_btn = Button(
           text="Attendance",
           command=self.attendence,
           cursor="hand2",
          bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        attendance_btn.place(x=900, y=100, width=250, height=60)





    #HELP BUTTON 
        help_btn = Button(
            text="Help",
            command=self.help_data,
            cursor="hand2",
            bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        help_btn.place(x=1250, y=100, width=250, height=60)




    #TRAIN DATA BUTTON
        train_btn = Button(
          text="Train Data",
          cursor="hand2",
          command=self.train_data,
          bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        train_btn.place(x=200, y=250, width=250, height=60)

    #PHOTOS BUTTON
        photos_btn = Button(
          text="Photos",
          cursor="hand2",
          command=self.open_image,
          bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        photos_btn.place(x=550, y=250, width=250, height=60)

    #DEVELOPER BUTTON
        developer_btn = Button(
            text="Developer",
            command=self.developer,
            cursor="hand2",
            bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold")
        )

        developer_btn.place(x=900, y=250, width=250, height=60)

    #EXIT BUTTON
        exit_btn = Button(
            text="Exit",
            cursor="hand2",
           bg="#2563EB",
            fg="white",
            activebackground="#1E40AF",
            font=("Segoe UI", 14, "bold"),
            command=self.root.destroy
        )

        exit_btn.place(x=1250, y=250, width=250, height=60)
        
        welcome_lbl = Label(    
        self.root,
        text="Welcome to Face Recognition Attendance System",
        font=("Segoe UI", 18, "bold"),
        bg="#F1F5F9",
        fg="#111827"
        )

        welcome_lbl.place(x=450, y=420)


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

        footer.place(x=-200, y=740, width=1920, height=50)

    def open_image(self):
        os.startfile("Face data")


        #function button 
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.Std=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.Std=Train(self.new_window)

    def face_recognation(self):
        self.new_window=Toplevel(self.root)
        self.Std=Face_Recognition(self.new_window)

    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.Std=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.Std=Developer(self.new_window)
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)









#MAIN
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()