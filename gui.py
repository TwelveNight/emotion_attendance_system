import tkinter as tk
from user_registration import register_user
from attendance import check_in, check_out, view_attendance

def create_gui():
    root = tk.Tk()
    root.title("Emotion-based Attendance System")

    tk.Button(root, text="Register User", command=register_user).pack()
    tk.Button(root, text="Check In", command=check_in).pack()
    tk.Button(root, text="Check Out", command=check_out).pack()
    tk.Button(root, text="View Attendance", command=view_attendance).pack()

    root.mainloop()
