from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector


class Face_Recognition:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#F1F5F9")

        # ================= TITLE =================
        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )

        title_lbl.place(x=-200, y=0, width=1920, height=50)

        # ================= BUTTON =================
        detect_btn = Button(
            self.root,
            text="START FACE RECOGNITION",
            command=self.face_recog,
            cursor="hand2",
            font=("Segoe UI", 16, "bold"),
            bg="#16A34A",
            fg="white",
            activebackground="#15803D"
        )

        detect_btn.place(x=600, y=300, width=300, height=80)


        info_lbl = Label(
            self.root,
            text="Press ENTER to stop recognition",
            font=("Segoe UI", 12),
            bg="#F1F5F9",
            fg="gray"
        )

        info_lbl.place(x=650, y=400)

    # ================= ATTENDANCE =================
    # ================= ATTENDANCE =================
    def mark_attendance(self, i, n, r, d):

        from datetime import datetime
        import os

        # Create Attendance folder
        if not os.path.exists("Attendance"):
            os.makedirs("Attendance")

        # Today's file name
        today_file = datetime.now().strftime("%d-%m-%Y") + ".csv"

        file_path = os.path.join("Attendance", today_file)

        # Create file if not exists
        if not os.path.exists(file_path):

            with open(file_path, "w", newline="\n") as f:

                f.write(
                    "Student_ID,Name,Roll,Department,Time,Date,Attendance\n"
                )

        with open(file_path, "r+", newline="\n") as f:

            myDataList = f.readlines()

            attendance_marked = False

            for line in myDataList[1:]:

                entry = line.strip().split(",")

                if len(entry) > 0:

                    if entry[0] == str(i):

                        attendance_marked = True
                        break

            # Mark attendance only once per day
            if not attendance_marked:

                now = datetime.now()

                d1 = now.strftime("%d/%m/%Y")

                dtString = now.strftime("%H:%M:%S")

                attendance_line = (
                    f"{i},{n},{r},{d},{dtString},{d1},Present\n"
                )

                f.write(attendance_line)

                print("Attendance Saved:", attendance_line)
 
    # ================= FACE RECOGNITION =================
    def face_recog(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            features = classifier.detectMultiScale(
                gray_image,
                scaleFactor,
                minNeighbors
            )

            coord = []

            for (x, y, w, h) in features:

                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)

                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100 * (1 - predict / 300)))

                # ================= DATABASE =================
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="0258",
                    database="face_recognation"
                )

                my_cursor = conn.cursor()

                my_cursor.execute(
                    "SELECT Name FROM student WHERE Student_id=%s",
                    (str(id),)
                )

                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute(
                    "SELECT Roll FROM student WHERE Student_id=%s",
                    (str(id),)
                )

                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute(
                    "SELECT Student_id FROM student WHERE Student_id=%s",
                    (str(id),)
                )

                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"


                my_cursor.execute(
                        "SELECT Dep FROM student WHERE Student_id=%s",
                        (str(id),)
                )

                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                conn.close()

                # ================= RECOGNITION =================
                if confidence > 65:

                    cv2.putText(
                        img,
                        f"ID: {i}",
                        (x, y-75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Name: {n}",
                        (x, y-45),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Roll: {r}",
                        (x, y-15),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Department: {d}",
                        (x, y+10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )
                    self.mark_attendance(i, n, r, d)
                

                else:

                    cv2.rectangle(
                        img,
                        (x, y),
                        (x+w, y+h),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y-10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):

            coord = draw_boundary(
                img,
                faceCascade,
                1.1,
                10,
                (255, 25, 255),
                "Face",
                clf
            )

            return img

        # ================= LOAD CASCADE =================
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml"
        )

        # ================= LOAD TRAINED MODEL =================
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.read("classifier.xml")

        # ================= START CAMERA =================
        video_cap = cv2.VideoCapture(0)

        while True:

            ret, img = video_cap.read()

            if not ret:
                break

            img = recognize(img, clf, faceCascade)

            cv2.imshow("Face Recognition", img)

            # press ENTER to close
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()

        cv2.destroyAllWindows()
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


# ================= MAIN =================
if __name__ == "__main__":

    root = Tk()

    obj = Face_Recognition(root)

    root.mainloop()