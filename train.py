from tkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.configure(bg="#F1F5F9")

        # ================= TITLE =================
        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("Segoe UI", 24, "bold"),
            bg="#1E3A8A",
            fg="white"
        )

        title_lbl.place(x=-200, y=0, width=1920, height=50)

        self.info_label = Label(
            self.root,
            text="Ready To Train Dataset",
            font=("Segoe UI", 14, "bold"),
            bg="#F1F5F9",
            fg="#111827"
        )

        self.info_label.place(x=630, y=220)

        # ================= TRAIN BUTTON =================
        train_btn = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            font=("Times New Roman", 25, "bold"),
            bg="green",
            fg="white"
        )

        train_btn.place(x=600, y=300, width=300, height=80)

# ================= PROGRESS BAR =================
        self.progress_label = Label(
            self.root,
            text="0%",
            font=("Segoe UI", 15, "bold"),
            bg="white",
            fg="green"
        )

        self.progress_label.place(x=730, y=400)

        self.progress_bar = ttk.Progressbar(
            self.root,
            orient=HORIZONTAL,
            length=400,
            mode='determinate'
        )

        self.progress_bar.place(x=550, y=450)

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


    # ================= TRAIN CLASSIFIER =================
    def train_classifier(self):

        try:

            data_dir = "Face data"

            path = []

            for file in os.listdir(data_dir):

                if file.endswith(".jpg") or file.endswith(".png"):

                    path.append(os.path.join(data_dir, file))

            total_images = len(path)

            print("Total Images Found:", total_images)

            faces = []
            ids = []

            if total_images == 0:

                messagebox.showerror(
                    "Error",
                    "No images found in Face data folder"
                )

                return

            for index, image in enumerate(path):

                try:

                    img = Image.open(image).convert('L')

                    img = img.resize((450, 450))

                    imageNp = np.array(img, 'uint8')

                    filename = os.path.split(image)[1]

                    id = int(filename.split('.')[1])

                    faces.append(imageNp)

                    ids.append(id)

                    # ================= UPDATE PROGRESS =================
                    progress_value = int(((index + 1) / total_images) * 100)

                    self.progress_bar["value"] = progress_value

                    self.progress_label.config(
                        text=f"{progress_value}%"
                    )

                    self.root.update_idletasks()

                except Exception as e:

                    print("Skipped File:", image)

                    print("Image Error:", e)

            ids = np.array(ids)

            clf = cv2.face.LBPHFaceRecognizer_create()

            clf.train(faces, ids)

            clf.write("classifier.xml")

            self.progress_bar["value"] = 100

            self.progress_label.config(text="Training Complete ✅")

            messagebox.showinfo(
                "Result",
                "Training datasets completed successfully"
            )

        except Exception as e:

            print("MAIN ERROR:", e)

            messagebox.showerror(
                "Error",
                f"{str(e)}"
            )
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

    obj = Train(root)

    root.mainloop()