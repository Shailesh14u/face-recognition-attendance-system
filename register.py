from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1000x650+250+50")
        self.root.title("Register User")
        self.root.configure(bg="#F1F5F9")



        # ================= VARIABLES =================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_username = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="CREATE NEW ACCOUNT",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white",
            pady=15
        )

        title.pack(fill=X)

        # ================= MAIN CARD =================
        main_frame = Frame(
            self.root,
            bg="white",
            bd=3,
            relief=RIDGE
        )

        main_frame.place(
            x=150,
            y=100,
            width=700,
            height=450
        )

        # First Name
        Label(main_frame,text="First Name",font=("Segoe UI",11,"bold"),bg="white").place(x=50,y=40)
        ttk.Entry(main_frame,textvariable=self.var_fname,width=25).place(x=50,y=70)

        # Last Name
        Label(main_frame,text="Last Name",font=("Segoe UI",11,"bold"),bg="white").place(x=380,y=40)
        ttk.Entry(main_frame,textvariable=self.var_lname,width=25).place(x=380,y=70)

        # Username
        Label(main_frame,text="Username",font=("Segoe UI",11,"bold"),bg="white").place(x=50,y=120)
        ttk.Entry(main_frame,textvariable=self.var_username,width=25).place(x=50,y=150)

        # Email
        Label(main_frame,text="Email",font=("Segoe UI",11,"bold"),bg="white").place(x=380,y=120)
        ttk.Entry(main_frame,textvariable=self.var_email,width=25).place(x=380,y=150)

        # Security Question
        Label(main_frame,text="Security Question",font=("Segoe UI",11,"bold"),bg="white").place(x=50,y=200)

        security_combo = ttk.Combobox(
            main_frame,
            textvariable=self.var_securityQ,
            width=23,
            state="readonly"
        )

        security_combo["values"] = (
            "Select",
            "Your Birth Place",
            "Your Pet Name",
            "Your Favourite Teacher"
        )

        security_combo.current(0)

        security_combo.place(x=50,y=230)

        # Security Answer
        Label(main_frame,text="Security Answer",font=("Segoe UI",11,"bold"),bg="white").place(x=380,y=200)
        ttk.Entry(main_frame,textvariable=self.var_securityA,width=25).place(x=380,y=230)

        # Password
        Label(main_frame,text="Password",font=("Segoe UI",11,"bold"),bg="white").place(x=50,y=280)

        self.password_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_password,
            width=25,
            show="*"
        )

        self.password_entry.place(x=50,y=310)

        # Confirm Password
        Label(main_frame,text="Confirm Password",font=("Segoe UI",11,"bold"),bg="white").place(x=380,y=280)

        self.confirm_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_confirmpassword,
            width=25,
            show="*"
        )

        self.confirm_entry.place(x=380,y=310)

        # Show Password
        self.show_pass = IntVar()

        Checkbutton(
            main_frame,
            text="Show Password",
            variable=self.show_pass,
            command=self.toggle_password,
            bg="white",
            font=("Segoe UI",10)
        ).place(x=280,y=350)

        # Register Button
        Button(
            main_frame,
            text="REGISTER",
            command=self.register_data,
            font=("Segoe UI",11,"bold"),
            bg="#16A34A",
            fg="white",
            cursor="hand2"
        ).place(x=180,y=390,width=140,height=40)

        # Reset Button
        Button(
            main_frame,
            text="RESET",
            command=self.reset_data,
            font=("Segoe UI",11,"bold"),
            bg="#F59E0B",
            fg="white",
            cursor="hand2"
        ).place(x=380,y=390,width=140,height=40)

        # Footer
        footer = Label(
            self.root,
            text="Face Recognition Attendance System | Developed by Shailesh Maurya",
            font=("Segoe UI",10),
            bg="#F1F5F9",
            fg="gray"
        )

        footer.pack(side=BOTTOM,pady=10)

    def toggle_password(self):

        if self.show_pass.get() == 1:

            self.password_entry.config(show="")
            self.confirm_entry.config(show="")

        else:

            self.password_entry.config(show="*")
            self.confirm_entry.config(show="*")

    # ================= REGISTER =================
    def register_data(self):

        if (
            self.var_fname.get() == "" or
            self.var_username.get() == "" or
            self.var_email.get() == "" or
            self.var_securityQ.get() == "Select" or
            self.var_password.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "All Fields Are Required",
                parent=self.root
            )

        elif self.var_password.get() != self.var_confirmpassword.get():

            messagebox.showerror(
                "Error",
                "Password & Confirm Password Must Be Same",
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
                    "SELECT * FROM register WHERE username=%s",
                    (self.var_username.get(),)
                )

                row = my_cursor.fetchone()

                if row is not None:

                    messagebox.showerror(
                        "Error",
                        "Username Already Exists",
                        parent=self.root
                    )

                else:

                    my_cursor.execute(
                        """
                        INSERT INTO register
                        (fname,lname,username,email,securityQ,securityA,password)
                        VALUES(%s,%s,%s,%s,%s,%s,%s)
                        """,
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_username.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_password.get()
                        )
                    )

                    conn.commit()

                    messagebox.showinfo(
                        "Success",
                        "Registration Successful",
                        parent=self.root
                    )

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )

    # ================= RESET =================
    def reset_data(self):

        self.var_fname.set("")
        self.var_lname.set("")
        self.var_username.set("")
        self.var_email.set("")
        self.var_securityQ.set("Select")
        self.var_securityA.set("")
        self.var_password.set("")
        self.var_confirmpassword.set("")


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = Register(root)

    root.mainloop()