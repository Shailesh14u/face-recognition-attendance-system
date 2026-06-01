from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class ForgotPassword:

    def __init__(self, root):

        self.root = root
        self.root.geometry("800x550+350+100")
        self.root.title("Forgot Password")
        self.root.configure(bg="#F1F5F9")

        # Variables
        self.var_username = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_newpassword = StringVar()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="RESET PASSWORD",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=15
        )

        title.pack(fill=X)

        # ================= CARD =================
        main_frame = Frame(
            self.root,
            bg="white",
            bd=3,
            relief=RIDGE
        )

        main_frame.place(
            x=180,
            y=100,
            width=450,
            height=320
        )

        # Username
        Label(
            main_frame,
            text="Username",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).place(x=40, y=30)

        ttk.Entry(
            main_frame,
            textvariable=self.var_username,
            width=35
        ).place(x=40, y=60)

        # Security Question
        Label(
            main_frame,
            text="Security Question",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).place(x=40, y=100)

        security_combo = ttk.Combobox(
            main_frame,
            textvariable=self.var_securityQ,
            width=32,
            state="readonly"
        )

        security_combo["values"] = (
            "Select",
            "Your Birth Place",
            "Your Pet Name",
            "Your Favourite Teacher"
        )

        security_combo.current(0)

        security_combo.place(x=40, y=130)

        # Security Answer
        Label(
            main_frame,
            text="Security Answer",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).place(x=40, y=170)

        ttk.Entry(
            main_frame,
            textvariable=self.var_securityA,
            width=35
        ).place(x=40, y=200)

        # New Password
        Label(
            main_frame,
            text="New Password",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).place(x=40, y=240)

        ttk.Entry(
            main_frame,
            textvariable=self.var_newpassword,
            width=35,
            show="*"
        ).place(x=40, y=270)

        # Reset Button
        Button(
            self.root,
            text="RESET PASSWORD",
            command=self.reset_password,
            font=("Segoe UI", 11, "bold"),
            bg="#16A34A",
            fg="white",
            cursor="hand2"
        ).place(
            x=300,
            y=450,
            width=220,
            height=45
        )

        # Footer
        footer = Label(
            self.root,
            text="Face Recognition Attendance System | Developed by Shailesh Maurya",
            font=("Segoe UI", 10),
            bg="#F1F5F9",
            fg="gray"
        )

        footer.pack(side=BOTTOM, pady=10)

    # ================= RESET PASSWORD =================
    def reset_password(self):

        if (
            self.var_username.get() == "" or
            self.var_securityQ.get() == "Select" or
            self.var_securityA.get() == "" or
            self.var_newpassword.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "All Fields Are Required",
                parent=self.root
            )

            return

        try:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="0258",
                database="face_recognation"
            )

            my_cursor = conn.cursor()

            my_cursor.execute(
                """
                SELECT * FROM register
                WHERE username=%s
                AND securityQ=%s
                AND securityA=%s
                """,
                (
                    self.var_username.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get()
                )
            )

            row = my_cursor.fetchone()

            if row is None:

                messagebox.showerror(
                    "Error",
                    "Invalid Details",
                    parent=self.root
                )

            else:

                my_cursor.execute(
                    """
                    UPDATE register
                    SET password=%s
                    WHERE username=%s
                    """,
                    (
                        self.var_newpassword.get(),
                        self.var_username.get()
                    )
                )

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Password Reset Successfully",
                    parent=self.root
                )

                self.root.destroy()

            conn.close()

        except Exception as es:

            messagebox.showerror(
                "Error",
                f"Due To : {str(es)}",
                parent=self.root
            )


if __name__ == "__main__":

    root = Tk()

    obj = ForgotPassword(root)

    root.mainloop()