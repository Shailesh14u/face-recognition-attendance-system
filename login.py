from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from register import Register


class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1000x600+250+100")
        self.root.configure(bg="#F1F5F9")

        # ================= TITLE =================
        title = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=15
        )
        title.pack(fill=X)

        # ================= MAIN LOGIN CARD =================
        login_frame = Frame(
            self.root,
            bg="white",
            bd=3,
            relief=RIDGE
        )

        login_frame.place(
            x=320,
            y=120,
            width=360,
            height=400
        )

        Label(
            login_frame,
            text="🔐 LOGIN",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#1E3A8A"
        ).pack(pady=20)

        # Username
        Label(
            login_frame,
            text="Username",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).pack(anchor="w", padx=30)

        self.txtuser = ttk.Entry(
            login_frame,
            font=("Segoe UI", 11)
        )

        self.txtuser.pack(
            padx=30,
            fill=X,
            pady=5
        )

        # Password
        Label(
            login_frame,
            text="Password",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).pack(anchor="w", padx=30, pady=(10, 0))

        self.txtpass = ttk.Entry(
            login_frame,
            font=("Segoe UI", 11),
            show="*"
        )

        self.txtpass.pack(
            padx=30,
            fill=X,
            pady=5
        )

        # Show Password
        self.show_pass = IntVar()

        Checkbutton(
            login_frame,
            text="Show Password",
            variable=self.show_pass,
            command=self.toggle_password,
            bg="white",
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=30)

        # Login Button
        Button(
            login_frame,
            text="LOGIN",
            command=self.login,
            font=("Segoe UI", 11, "bold"),
            bg="#1E3A8A",
            fg="white",
            cursor="hand2"
        ).pack(
            fill=X,
            padx=30,
            pady=15
        )

        # Register Button
        Button(
            login_frame,
            text="New User Register",
            command=self.register_window,
            font=("Segoe UI", 10, "bold"),
            bg="#16A34A",
            fg="white",
            cursor="hand2"
        ).pack(
            fill=X,
            padx=30,
            pady=5
        )

        # Forgot Password
        Button(
            login_frame,
            text="Forgot Password?",
            command=self.forgot_password_window,
            font=("Segoe UI", 10, "bold"),
            bg="#DC2626",
            fg="white",
            cursor="hand2"
        ).pack(
            fill=X,
            padx=30,
            pady=5
        )

        # ================= FOOTER =================
        footer = Label(
            self.root,
            text="Developed By Shailesh Maurya | Version 1.0",
            font=("Segoe UI", 10),
            bg="#F1F5F9",
            fg="gray"
        )

        footer.pack(side=BOTTOM, pady=15)

    # ================= SHOW PASSWORD =================
    def toggle_password(self):

        if self.show_pass.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ================= LOGIN =================
    def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":

            messagebox.showerror(
                "Error",
                "All Fields Are Required",
                parent=self.root
            )

        else:

            try:

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="0258",
                    database="face_recognation"
                )

                my_cursor = conn.cursor()

                my_cursor.execute(
                    "SELECT * FROM register WHERE username=%s AND password=%s",
                    (
                        self.txtuser.get(),
                        self.txtpass.get()
                    )
                )

                row = my_cursor.fetchone()

                if row is None:

                    messagebox.showerror(
                        "Error",
                        "Invalid Username or Password"
                    )

                else:

                    messagebox.showinfo(
                        "Success",
                        "Login Successful"
                    )

                    self.root.destroy()

                    from main import Face_Recognition_System

                    root = Tk()

                    obj = Face_Recognition_System(root)

                    root.mainloop()

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}"
                )

    # ================= REGISTER =================
    def register_window(self):

        from register import Register

        self.new_window = Toplevel(self.root)

        self.app = Register(self.new_window)

    # ================= FORGOT PASSWORD =================
    def forgot_password_window(self):

        from forgot_password import ForgotPassword

        self.new_window = Toplevel(self.root)

        self.app = ForgotPassword(self.new_window)


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = Login(root)

    root.mainloop()