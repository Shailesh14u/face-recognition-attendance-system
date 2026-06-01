from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog
import shutil
from datetime import date
import re
from tkcalendar import DateEntry
import os



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.configure(bg="#F1F5F9")



        # ================= VARIABLES =================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()

        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_search = StringVar()
        self.var_search_txt = StringVar()
       

        #TITLE
        title_lbl = Label(
            self.root,
            text="STUDENT MANAGEMANET",
           font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )
        title_lbl.place(x=-200, y=0, width=1920, height=50)

        # main frame 
        main_frame = Frame(self.root, bd=0,bg="#F1F5F9")
        main_frame.place(x=10, y=60, width=1500, height=700)

        # LEft Frame 
        left_frame = LabelFrame(
           main_frame,
           bd=3,
           bg="white",
           relief=RIDGE,
           text="Student Details",
           font=("Segoe UI", 12, "bold")
        )

        left_frame.place(x=10, y=10, width=730, height=670)

        # Current Frame 
        current_course_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("Segoe UI", 12, "bold")
        )

        current_course_frame.place(x=5, y=10, width=700, height=150)


        # Department
        dep_label = Label(
           current_course_frame,
           text="Department",
           font=("Segoe UI", 12, "bold"),
           bg="white"
        )

        dep_label.grid(row=0, column=0)

        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
            width=18
        )

        dep_combo["values"] = (
            "Select Department",
            "Computer Engineering",
            "AI & ML",
            "AI & DS",
            "Information Technology",
            "Mechanical Engineering",
            "Civil Engineering"
        )
        dep_combo.current(0)

        dep_combo.grid(row=0, column=1, padx=2, sticky=W)


        # Year 
        year_label = Label(
            current_course_frame,
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        year_label.grid(row=0, column=2, padx=10, pady=15)

        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
            width=18
        )

        year_combo["values"] = (
            "Select Course",
            "FE",
            "SE",
            "TE",
            "BE",
        )

        year_combo.current(0)

        year_combo.grid(row=0, column=3, padx=10, pady=15)



        # Academy Year 
        acc_year_label = Label(
            current_course_frame,
            text="Academic Year",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        acc_year_label.grid(row=1, column=0, padx=10, pady=15)

        acc_year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
            width=18
        )

        acc_year_combo["values"] = (
            "Select Year",
            "2023-24",
            "2024-25",
            "2025-26",
            "2026-27"
        )

        acc_year_combo.current(0)

        acc_year_combo.grid(row=1, column=1, padx=10, pady=15)



        #SEMESTER
        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        semester_label.grid(row=1, column=2, padx=10, pady=15)

        semester_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
            width=18
        )

        semester_combo["values"] = (
            "Select Semester",
            "Semester-1",
            "Semester-2",
            "Semester-3",
            "Semester-4",
            "Semester-5",
            "Semester-6",
            "Semester-7",
            "Semester-8"
        )

        semester_combo.current(0)

        semester_combo.grid(row=1, column=3, padx=10, pady=15)

        # class student frame 
        class_student_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Information",
            font=("Segoe UI", 12, "bold")
        )

        class_student_frame.place(x=5, y=170, width=700, height=400)

        # ================= STUDENT ID =================
        studentId_label = Label(
            class_student_frame,
            text="Student ID",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_id,
            width=20,
            font=("Times New Roman", 12, "bold"),
            state="readonly"
        )

        studentId_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

# ================= STUDENT NAME =================
        studentName_label = Label(
            class_student_frame,
            
            text="Student Name",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        studentName_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        studentName_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

# ================= CLASS DIVISION =================
        classDiv_label = Label(
            class_student_frame,
           
            text="Class Division",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        classDiv_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        classDiv_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_div,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        classDiv_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

# ================= ROLL NUMBER =================
        rollNo_label = Label(
            class_student_frame,
            
            text="Roll Number",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        rollNo_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        rollNo_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        rollNo_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

# ================= GENDER =================
        gender_label = Label(
            class_student_frame,
            
            text="Gender",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
             width=18
        )

        gender_combo["values"] = (
            "Select Gender",
            "Male",
            "Female",
            "Other"
        )

        gender_combo.current(0)

        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

# ================= DOB =================
        dob_label = Label(
            class_student_frame,
            
            text="DOB",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        dob_entry = DateEntry(
            class_student_frame,
            textvariable=self.var_dob,
            width=18,
            font=("Segoe UI", 11),
            date_pattern="dd/mm/yyyy",
            maxdate=date.today(),
            state="readonly"
        )

        dob_entry.grid(
            row=2,
            column=3,
            padx=10,
            pady=10,
            sticky=W
        )

        

# ================= EMAIL =================
        email_label = Label(
            class_student_frame,
            
            text="Email",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# ================= PHONE =================
        phone_label = Label(
            class_student_frame,
            
            text="Phone",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
             width=20,
            font=("Times New Roman", 12, "bold")
        )

        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

# ================= ADDRESS =================
        address_label = Label(
            class_student_frame,
            
            text="Address",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        address_entry = ttk.Entry(
             class_student_frame,
             textvariable=self.var_address,
            width=50,
            font=("Times New Roman", 12, "bold")
        )

        address_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky=W)



    # radio button 
        self.var_radio1 = StringVar()
        
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            text="Take Photo Sample",
            variable=self.var_radio1,
            value="Yes"
        )

        radiobtn1.grid(row=5, column=0, padx=10, pady=15, sticky=W)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            text="No Photo Sample",
            variable=self.var_radio1,
            
            value="No"
        )

        radiobtn2.grid(row=5, column=1, padx=10, pady=15, sticky=W)




        # button frame 
        btn_frame=Frame(
            class_student_frame,
            bd=2,
            relief=RIDGE,
            bg="white",

        )

        btn_frame.place(x=5, y=290, width=680, height=50)


        # ================= SAVE BUTTON =================
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=18,
            font=("Segoe UI", 10, "bold"),
             bg="#2563EB",
            fg="white"
        )

        save_btn.grid(row=0, column=0)

# ================= UPDATE BUTTON =================
        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=18,
            font=("Segoe UI", 10, "bold"),
            bg="#16A34A",
            fg="white"
        )

        update_btn.grid(row=0, column=1)

# ================= DELETE BUTTON =================
        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=18,
            font=("Segoe UI", 10, "bold"),
            bg="red",
            fg="white"
        )

        delete_btn.grid(row=0, column=2)

# ================= RESET BUTTON =================
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=18,
            font=("Segoe UI", 10, "bold"),
            bg="#F59E0B",
            fg="white"
        )

        reset_btn.grid(row=0, column=3)




        # ================= PHOTO SAMPLE BUTTON FRAME =================
        btn_frame1 = Frame(
            class_student_frame,
             bd=2,
            relief=RIDGE,
            bg="white"
        )

        btn_frame1.place(x=5, y=340, width=680, height=50)

# ================= TAKE PHOTO SAMPLE BUTTON =================
        take_photo_btn = Button(
            btn_frame1,
            text="Take Photo Sample",
            command=self.generate_dataset,
            width=37,
            font=("Segoe UI", 10, "bold"),
            bg="#1E3A8A",
            fg="white"
        )

        take_photo_btn.grid(row=0, column=0)
        

# ================= UPDATE PHOTO SAMPLE BUTTON =================
        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            width=37,
            command=self.upload_photo_sample,
            font=("Segoe UI", 10, "bold"),
            bg="#059669",
            fg="white"
        )

        update_photo_btn.grid(row=0, column=1)



        # Right Frame 
        right_frame = LabelFrame(
           main_frame,
           bd=2,
           bg="white",
           relief=RIDGE,
           text="Student Records",
           font=("Times New Roman", 15, "bold")
        )

        right_frame.place(x=750, y=10, width=730, height=670)


        # Search system 
        search_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("Segoe UI", 12, "bold")
        )

        search_frame.place(x=5, y=10, width=700, height=70)



        # SEARCH COMBOBOX
        search_combo = ttk.Combobox(
            search_frame,
            textvariable=self.var_search,
            font=("Times New Roman", 12, "bold"),
             state="readonly",
             width=15
        )

        search_combo["values"] = (
            "Select",
            "Roll No",
            "Phone No"
        )

        search_combo.current(0)

        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

#  SEARCH ENTRY 
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.var_search_txt,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)


        # ================= SEARCH BUTTON =================
        search_btn = Button(
            search_frame,
            text="Search",
            command=self.search_data,
            width=12,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white"
        )

        search_btn.grid(row=0, column=3, padx=5)

# ================= SHOW ALL BUTTON =================
        showAll_btn = Button(
            search_frame,
            text="Show All",
            command=self.fetch_data,
            width=12,
            font=("Times New Roman", 12, "bold"),
            bg="green",
            fg="white"
        )

        showAll_btn.grid(row=0, column=4, padx=5)



       # ================= TABLE FRAME =================
        table_frame = Frame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE
        )

        table_frame.place(x=5, y=100, width=710, height=550)

# ================= SCROLL BAR =================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

# ================= TABLE STYLE =================
        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )




# ================= STUDENT TABLE =================
        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "photo"
           ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

# ================= TABLE HEADINGS ================
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email ")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")

# ================= COLUMN WIDTH =================
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.generate_student_id()


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


    def generate_student_id(self):

        try:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="0258",
                database="face_recognation"
            )

            my_cursor = conn.cursor()

            my_cursor.execute(
                "SELECT MAX(Student_id) FROM student"
            )

            result = my_cursor.fetchone()

            if result[0] is None:

                self.var_std_id.set("1001")

            else:

                self.var_std_id.set(
                    str(int(result[0]) + 1)
                )

            conn.close()

        except Exception as es:

            print(es)

        

# ADD  data function 
    def add_data(self):

        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "Please Select Department", parent=self.root)
            return

        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID Required",parent=self.root)
            return

        if self.var_std_name.get() == "":
            messagebox.showerror("Error", "Student Name Required",parent=self.root)
            return

        if not self.var_phone.get().isdigit():
            messagebox.showerror(
                "Error",
                "Phone must contain only numbers",
                parent=self.root
            )
            return

        if len(self.var_phone.get()) != 10:
            messagebox.showerror(
                "Error",
                "Phone number must be 10 digits",
                parent=self.root
            )
            return

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror(
                "Error",
                "Invalid Email Address",
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
                INSERT INTO student
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()
                )
            )

            conn.commit()

            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Success",
                "Student Details Added Successfully",
                parent=self.root
            )

            self.reset_data()

        except Exception as es:

            messagebox.showerror(
                "Error",
                f"Due To : {str(es)}",
                parent=self.root
            )

    # fetch data 
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="0258",
                    database="face_recognation"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from  student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def search_data(self):

        if self.var_search.get() == "Select" or self.var_search_txt.get() == "":

            messagebox.showerror(
                "Error",
                "Please select search option and enter value",
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

                if self.var_search.get() == "Roll No":

                    my_cursor.execute(
                        "SELECT * FROM student WHERE Roll=%s",
                        (self.var_search_txt.get(),)
                    )

                elif self.var_search.get() == "Phone No":

                    my_cursor.execute(
                        "SELECT * FROM student WHERE Phone=%s",
                        (self.var_search_txt.get(),)
                    )

                rows = my_cursor.fetchall()

                if len(rows) != 0:

                    self.student_table.delete(
                        *self.student_table.get_children()
                    )

                    for row in rows:

                        self.student_table.insert(
                            "",
                            END,
                            values=row
                        )

                else:

                    messagebox.showinfo(
                        "Result",
                        "No Record Found",
                        parent=self.root
                    )

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )
        


# Get cursor 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])

        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_radio1.set(data[13])                



# update function 
    def update_data(self):

        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:

                update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details?",
                    parent=self.root
                )

                if update:

                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="0258",
                        database="face_recognation"
                    )

                    my_cursor = conn.cursor()

                    sql = """
                    UPDATE student SET
                    Dep=%s,
                    course=%s,
                    Year=%s,
                    Semester=%s,
                    Name=%s,
                    Division=%s,
                    Roll=%s,
                    Gender=%s,
                    Dob=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    PhotoSample=%s
                    WHERE Student_id=%s
                    """

                    val = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )
                    print(self.var_std_id.get())

                    my_cursor.execute(sql, val)

                    
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )


    def delete_data(self):

        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error",
                "Student ID is required",
                parent=self.root
            )

        else:
            try:

                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student?",
                    parent=self.root
                )

                if delete > 0:

                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="0258",
                        database="face_recognation"
                    )

                    my_cursor = conn.cursor()

                    sql = "DELETE FROM student WHERE Student_id=%s"

                    val = (self.var_std_id.get(),)

                    my_cursor.execute(sql, val)

                    conn.commit()

                    self.fetch_data()

                    conn.close()

                    messagebox.showinfo(
                        "Delete",
                        "Successfully deleted student details",
                        parent=self.root
                    )

                else:
                    return

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )

# Reset Function 
    def reset_data(self):

        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")

        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
        self.generate_student_id()



# Take Photo Sample
    # Take Photo Sample
    def generate_dataset(self):

        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error",
                "All Fields are required",
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
                    """
                    update student set
                    Dep=%s,
                    course=%s,
                    Year=%s,
                    Semester=%s,
                    Name=%s,
                    Division=%s,
                    Roll=%s,
                    Gender=%s,
                    Dob=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    PhotoSample=%s
                    where Student_id=%s
                    """,
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )
                )

                conn.commit()
                self.fetch_data()
                conn.close()

                # ================= FACE DETECTOR =================

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    faces = face_classifier.detectMultiScale(
                        gray,
                        1.3,
                        5
                    )

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)

                # ================= IMAGE COUNT =================
                existing_files = [
                    f for f in os.listdir("Face data")
                    if f.startswith(f"user.{self.var_std_id.get()}.")
                ]

                img_id = len(existing_files)

                while True:

                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:

                        img_id += 1

                        face = cv2.resize(
                            face_cropped(my_frame),
                            (450, 450)
                        )

                        face = cv2.cvtColor(
                            face,
                            cv2.COLOR_BGR2GRAY
                        )

                        file_name_path = (
                            "Face data/user."
                            + str(self.var_std_id.get())
                            + "."
                            + str(img_id)
                            + ".jpg"
                        )

                        cv2.imwrite(file_name_path, face)

                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2
                        )

                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result",
                    "Generating dataset completed",
                    parent=self.root
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )


# Upload Photo Sample
    def upload_photo_sample(self):

        if self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror(
                "Error",
                "Student ID and Name are required",
                parent=self.root
            )

        else:
            try:

                file_path = filedialog.askopenfilename(
                    title="Select Image",
                    filetypes=(
                        ("Image Files", "*.jpg *.jpeg *.png"),
                        ("All Files", "*.*")
                    )
                )

                if file_path:

                    if not os.path.exists("Face data"):
                        os.makedirs("Face data")

                    existing_files = [
                        f for f in os.listdir("Face data")
                        if f.startswith(f"user.{self.var_std_id.get()}.")
                    ]

                    img_no = len(existing_files) + 1

                    destination = (
                        f"Face data/user."
                        f"{self.var_std_id.get()}."
                        f"{img_no}.jpg"
                    )

                    shutil.copy(file_path, destination)

                    self.var_radio1.set("Yes")

                    messagebox.showinfo(
                        "Success",
                        "Photo uploaded successfully",
                        parent=self.root
                    )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )
    

















#MAIN
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()