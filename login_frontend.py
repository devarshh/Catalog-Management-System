import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from backend import validate_login


def create_login_screen(root, on_login_success):
    fg_color = "#FFFFFF"  # White text
    accent_color = "#FF5722"  # Orange accent
    input_bg = "#1E1E1E"  # Dark gray for inputs

    def on_eye_click():
        if password_entry.cget('show') == '*':
            password_entry.configure(show='')
        else:
            password_entry.configure(show='*')

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username and not password:
            messagebox.showerror(title="Invalid Username or Password", message="Please enter your username and password.")
            return
        if not username:
            messagebox.showerror(title="Invalid Username", message="Please enter your username.")
            return
        if not password:
            messagebox.showerror(title="Invalid Password", message="Please enter your password.")
            return


        if validate_login(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
            on_login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    # Clear any existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#121212")  # Dark background

    # Welcome Text
    welcome_label = tk.Label(root, text="Welcome Back User!", font=("Arial Bold", 35), fg=fg_color, bg="#242424")
    welcome_label.place(x=220, y=50)

    welcome_label = tk.Label(root, text="Sign In", font=("Arial Bold", 25), fg="#d1d1d1", bg="#242424")
    welcome_label.place(x=370, y=150)

    # Username Field
    username_entry = ctk.CTkEntry(root, font=("Arial", 14), corner_radius=8, fg_color=input_bg, text_color=fg_color,
                                  placeholder_text="Username or Email", width=357, height=40)  # Width and height set here
    username_entry.place(x=120, y=150)

    # Password Field
    password_entry = ctk.CTkEntry(root, font=("Arial", 14), corner_radius=8, fg_color=input_bg, text_color=fg_color,
                                  placeholder_text="Password", show="*", width=300, height=40)  # Width and height set here
    password_entry.place(x=120, y=210)

    # Eye Button for Password Visibility
    eye_button = ctk.CTkButton(root, text="👁", font=("Arial", 15), corner_radius=10, fg_color=input_bg,
                               text_color=fg_color, border_width=2, border_color="#4f4f4f", width=50, height=40, command=on_eye_click)
    eye_button.place(x=425, y=210)

    # Sign In Button
    sign_in_button = ctk.CTkButton(root, text="Sign In", font=("Arial Bold", 14), corner_radius=20,
                                   fg_color=accent_color, text_color=fg_color, command=handle_login, width=250, height=50)
    sign_in_button.place(x=175, y=340)
