from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import csv
import os


mydata = []


class Attendance:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance Management System")
        self.root.configure(bg="#F1F5F9")

        # ================= VARIABLES =================
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_attendance_file = StringVar()

        # ================= TITLE =================
        title_lbl = Label(
            self.root,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )

        title_lbl.place(x=-200, y=0, width=1920, height=50)

        self.current_file_lbl = Label(
            self.root,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="blue"
        )

        self.current_file_lbl.place(
            x=650,
            y=50
        )

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bd=0,bg="#F1F5F9")

        main_frame.place(x=10, y=60, width=1500, height=700)

        # ================= LEFT FRAME =================
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance Details",
            font=("Segoe UI", 12, "bold")
        )

        left_frame.place(x=10, y=10, width=730, height=650)

        # ================= LABELS & ENTRIES =================

        # Attendance ID
        attendanceId_label = Label(
            left_frame,
            text="Attendance ID:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceId_label.grid(row=0, column=0, padx=10, pady=10)

        attendanceId_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_id,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceId_entry.grid(row=0, column=1, padx=10, pady=10)

        # Name
        attendanceName_label = Label(
            left_frame,
            text="Name:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceName_label.grid(row=1, column=0, padx=10, pady=10)

        attendanceName_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_name,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceName_entry.grid(row=1, column=1, padx=10, pady=10)

        # Roll
        attendanceRoll_label = Label(
            left_frame,
            text="Roll:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceRoll_label.grid(row=2, column=0, padx=10, pady=10)

        attendanceRoll_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_roll,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceRoll_entry.grid(row=2, column=1, padx=10, pady=10)

        # Department
        attendanceDep_label = Label(
            left_frame,
            text="Department:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceDep_label.grid(row=3, column=0, padx=10, pady=10)

        attendanceDep_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_dep,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceDep_entry.grid(row=3, column=1, padx=10, pady=10)

        # Time
        attendanceTime_label = Label(
            left_frame,
            text="Time:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceTime_label.grid(row=4, column=0, padx=10, pady=10)

        attendanceTime_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_time,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceTime_entry.grid(row=4, column=1, padx=10, pady=10)

        # Date
        attendanceDate_label = Label(
            left_frame,
            text="Date:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceDate_label.grid(row=5, column=0, padx=10, pady=10)

        attendanceDate_entry = ttk.Entry(
            left_frame,
            textvariable=self.var_atten_date,
            width=20,
            font=("Times New Roman", 12, "bold")
        )

        attendanceDate_entry.grid(row=5, column=1, padx=10, pady=10)

        # Attendance Status
        attendanceStatus_label = Label(
            left_frame,
            text="Attendance:",
            font=("Segoe UI", 12, "bold"),
            bg="white"
        )

        attendanceStatus_label.grid(row=6, column=0, padx=10, pady=10)

        attendance_status = ttk.Combobox(
            left_frame,
            textvariable=self.var_atten_attendance,
            font=("Times New Roman", 12, "bold"),
            state="readonly",
            width=18
        )

        attendance_status["values"] = (
            "Status",
            "Present",
            "Absent"
        )

        attendance_status.current(0)

        attendance_status.grid(row=6, column=1, padx=10, pady=10)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(
            left_frame,
            bd=2,
            relief=RIDGE,
            bg="white"
        )

        btn_frame.place(x=10, y=400, width=700, height=50)

        # Import CSV
        import_btn = Button(
            btn_frame,
            text="Import CSV",
            command=self.importCsv,
            width=17,
            font=("Segoe UI", 12, "bold"),
            bg="blue",
            fg="white"
        )

        import_btn.grid(row=0, column=0)

        # Export CSV
        export_btn = Button(
            btn_frame,
            text="Export CSV",
            command=self.exportCsv,
            width=17,
            font=("Segoe UI", 12, "bold"),
            bg="green",
            fg="white"
        )

        export_btn.grid(row=0, column=1)

        # Reset
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=17,
            font=("Segoe UI", 12, "bold"),
            bg="orange",
            fg="white"
        )

        reset_btn.grid(row=0, column=2)

# ============Generate absents========
        generate_absent_btn = Button(
            btn_frame,
            text="Generate Absentees",
            command=self.generate_absentees,
            width=17,
            font=("Segoe UI", 12, "bold"),
            bg="#DC2626",
            fg="white",
            cursor="hand2"
        )

        generate_absent_btn.grid(row=0, column=3)

        # ================= RIGHT FRAME =================
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("Segoe UI", 12, "bold")
        )

        right_frame.place(x=750, y=10, width=720, height=650)


        # ================= STATISTICS FRAME =================
        stats_frame = Frame(
            right_frame,
            bg="white"
        )

        stats_frame.place(
            x=10,
            y=50,
            width=690,
            height=80
        )

        # Total Records
        self.total_lbl = Label(
            stats_frame,
            text="Total\n0",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=15,
            height=3
        )

        self.total_lbl.grid(row=0, column=0, padx=10)

        # Present
        self.present_lbl = Label(
            stats_frame,
            text="Present\n0",
            bg="#16A34A",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=15,
            height=3
        )

        self.present_lbl.grid(row=0, column=1, padx=10)

        # Absent
        self.absent_lbl = Label(
            stats_frame,
            text="Absent\n0",
            bg="#DC2626",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=15,
            height=3
        )

        self.absent_lbl.grid(row=0, column=2, padx=10)


        Label(
            right_frame,
            text="Select Date:",
            font=("Segoe UI", 10, "bold"),
            bg="white"
        ).place(x=10, y=10)

        self.date_combo = ttk.Combobox(
            right_frame,
            textvariable=self.var_attendance_file,
            width=25,
            state="readonly",
            font=("Segoe UI", 10, "bold")
        )

        self.date_combo.place(x=100, y=10)


# ============date Load button==========
        Button(
            right_frame,
            text="Load",
            command=self.load_selected_attendance,
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).place(x=320, y=8)

        # ================= TABLE FRAME =================
        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE,
            bg="white"
        )

        table_frame.place(x=10, y=120, width=690, height=500)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)


        # ================= TABLE STYLE =================
        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "name",
                "roll",
                "department",
                "time",
                "date",
                "attendance"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Headings
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.tag_configure(
            "oddrow",
            background="#F3F4F6"
        )

        self.AttendanceReportTable.tag_configure(
            "evenrow",
            background="white"
        )

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind(
        "<ButtonRelease>",
         self.get_cursor
        )
        self.load_available_dates()

# ========Footer======
        footer = Frame(
            self.root,
            bg="#1E3A8A"
        )

        footer.place(
            x=-200,
            y=740,
            width=1920,
            height=50
            )

        Label(
            footer,
            text="📧 Support: shailesh.m0825@gmail.com | Version: 1.0",
            font=("Segoe UI", 10, "bold"),
            bg="#1E3A8A",
            fg="white"
            ).pack(pady=10)


    # ================= FETCH DATA =================
       
    def fetchData(self, rows):

        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children()
        )

        count = 0

        for i in rows:

            if count % 2 == 0:

                self.AttendanceReportTable.insert(
                    "",
                    END,
                    values=i,
                    tags=("evenrow",)
                )

            else:

                self.AttendanceReportTable.insert(
                    "",
                    END,
                    values=i,
                    tags=("oddrow",)
                )

            count += 1
        self.update_statistics(rows)
# ===========Statistics Function==========
    def update_statistics(self, rows):

        total = len(rows)

        present = 0
        absent = 0

        for row in rows:

            if len(row) >= 7:

                if str(row[6]).lower() == "present":

                    present += 1

                elif str(row[6]).lower() == "absent":

                    absent += 1

        self.total_lbl.config(
            text=f"Total\n{total}"
        )

        self.present_lbl.config(
            text=f"Present\n{present}"
        )

        self.absent_lbl.config(
            text=f"Absent\n{absent}"
        )
    

    def get_cursor(self, event=""):

        cursor_row = self.AttendanceReportTable.focus()

        contents = self.AttendanceReportTable.item(cursor_row)

        row = contents["values"]

        if len(row) > 0:

            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])


# ===============Fill Dates Automatically============
    def load_available_dates(self):

            attendance_folder = "Attendance"

            if not os.path.exists(attendance_folder):
                return

            files = [
                f for f in os.listdir(attendance_folder)
                if f.endswith(".csv")
            ]

            files.sort(reverse=True)

            self.date_combo["values"] = files

            if len(files) > 0:

                self.date_combo.current(0)

                self.load_selected_attendance()


# ===============Load Selected File===============
    def load_selected_attendance(self):

            selected_file = self.var_attendance_file.get()

            if selected_file == "":
                return

            file_path = os.path.join(
                "Attendance",
                selected_file
            )

            with open(file_path, newline="") as f:

                csv_reader = csv.reader(f)

                data = list(csv_reader)

                if len(data) > 1:

                    self.fetchData(data[1:])



# ================= LOAD CSV AUTOMATICALLY =================
    def load_attendance_data(self):

        attendance_folder = "Attendance"

        if not os.path.exists(attendance_folder):

            return

        files = [
            os.path.join(attendance_folder, f)
            for f in os.listdir(attendance_folder)
            if f.endswith(".csv")
        ]

        if len(files) == 0:

            return

        latest_file = max(
            files,
            key=os.path.getctime
        )
        self.current_file_lbl.config(
            text=f"Showing: {os.path.basename(latest_file)}"
         )

        with open(latest_file, newline="") as f:

            csv_reader = csv.reader(f)

            data = list(csv_reader)

            if len(data) > 1:

                self.fetchData(data[1:])
                

    # ================= IMPORT CSV =================
    def importCsv(self):

        global mydata

        mydata.clear()

        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root
        )

        with open(fln) as myfile:

            csvread = csv.reader(myfile, delimiter=",")

            for i in csvread:
                mydata.append(i)

            self.fetchData(mydata)

    # ================= EXPORT CSV =================
    def exportCsv(self):

        try:

            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data",
                    "No data found to export",
                    parent=self.root
                )

                return False

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root
            )

            with open(fln, mode="w", newline="") as myfile:

                exp_write = csv.writer(myfile, delimiter=",")

                for i in mydata:
                    exp_write.writerow(i)

            messagebox.showinfo(
                "Data Export",
                "Your data exported successfully"
            )

        except Exception as es:

            messagebox.showerror(
                "Error",
                f"Due To: {str(es)}",
                parent=self.root
            )

    # ================= RESET =================
    def reset_data(self):

        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
    
# ==========Function generate_absentees=======
    def generate_absentees(self):

        try:

            import mysql.connector
            from datetime import datetime

            selected_file = self.var_attendance_file.get()

            if selected_file == "":

                messagebox.showerror(
                    "Error",
                    "Please select attendance date"
                )

                return

            file_path = os.path.join(
                "Attendance",
                selected_file
            )

            present_students = []

            with open(file_path, "r") as f:

                csv_reader = csv.reader(f)

                next(csv_reader, None)

                for row in csv_reader:

                    if len(row) > 0:

                        present_students.append(
                            str(row[0])
                        )

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="0258",
                database="face_recognation"
            )

            my_cursor = conn.cursor()

            my_cursor.execute(
                """
                SELECT Student_id,
                    Name,
                    Roll,
                    Dep
                FROM student
                """
            )

            students = my_cursor.fetchall()

            conn.close()

            current_date = datetime.now().strftime("%d/%m/%Y")

            with open(file_path, "a", newline="") as f:

                for student in students:

                    sid = str(student[0])

                    if sid not in present_students:

                        f.write(
                            f"{student[0]},"
                            f"{student[1]},"
                            f"{student[2]},"
                            f"{student[3]},"
                            f"00:00:00,"
                            f"{current_date},"
                            f"Absent\n"
                        )

            self.load_selected_attendance()

            messagebox.showinfo(
                "Success",
                "Absentees Generated Successfully"
            )

        except Exception as es:

            messagebox.showerror(
                "Error",
                str(es)
            )
        
        
# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = Attendance(root)

    root.mainloop()